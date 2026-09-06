# Importations des librairies nécessaires
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import requests
from datetime import datetime

# Fichiers générés
OUTPUT_PATH = "largest_banks_data.csv"
DB_NAME = "banks.db"
TABLE_NAME = "largest_banks"
LOG_FILE = "code_log.txt"

#Ce script permet d'écrire des messages sur le fichier log et d'horodater
def log_progress(message): 
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format) 
    with open(LOG_FILE,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Fonction d'extraction
def extract(url, table_attributs=None):
    # Récupération du tableau
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Erreur HTTP {response.status_code} sur {url}")
    data = BeautifulSoup(response.text, 'html.parser')
    # Si des attributs de table sont fournis, les utiliser
    if table_attributs:
        tables = data.find_all('table', table_attributs)
    else:
        tables = data.find_all('tbody')
    if not tables:
        raise ValueError("Aucune table trouvée sur la page")
    rows = tables[0].find_all('tr')
    # Collecte des données dans une liste (plus de warnings)
    data_list = []
    count = 0
    for row in rows:
        if count >= 10:
            break
        col = row.find_all('td')
        if len(col) >= 3:  # Vérifie qu'il y a au moins 3 colonnes
            data_list.append({
                "Name": str(col[1].get_text(strip=True)),
                "MC_USD_Billion": float(col[2].get_text(strip=True).replace(',', ''))
            })
            count += 1
    # Création du DataFrame à partir de la liste
    df = pd.DataFrame(data_list)
    return df

# Fonction de transformation des données
def transform(df, csv_path):
    # Extraction des données du fichier csv
    df2 = pd.read_csv(csv_path)
    # Transformation en dictionnaire clé/valeur
    rates = df2.set_index("Currency")["Rate"].to_dict()
    # Ajout des colonnes converties
    df["MC_EUR_Billion"] = (df["MC_USD_Billion"] * rates["EUR"]).round(2)
    df["MC_GBP_Billion"] = (df["MC_USD_Billion"] * rates["GBP"]).round(2)
    df["MC_INR_Billion"] = (df["MC_USD_Billion"] * rates["INR"]).round(2)
    return df
    
# Fonction de chargement des données sous format csv
def load_to_csv(df, OUTPUT_PATH):
    # Chargement des données dans le fichier csv
    df.to_csv(OUTPUT_PATH, index=False)
    log_progress(f"Data successfully saved to csv at {OUTPUT_PATH}")
    
# Fonction de chargement des données dans une db
def load_to_db(df, sql_connection, TABLE_NAME):
    # Chargement des données dans une base de données
    df.to_sql(TABLE_NAME, sql_connection, if_exists='replace', index=False)
    log_progress(f"Data successfully saved to database {DB_NAME} table {TABLE_NAME}")

# Fonction de requêtage sql
def run_query(query_statement, sql_connection):
    # Exécute une requête SQL et affiche les résultats
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_statement)
    print(query_output)
    log_progress(f"Query executed: {query_statement}")
    return query_output

#Début du processus ETL
log_progress("ETL Job Started") 
 
#Début de l'extraction
log_progress("Extract phase Started") 

url = (
    "https://web.archive.org/web/20230908091635/"
    "https://en.wikipedia.org/wiki/List_of_largest_banks"
)
data_extracted = extract(url)
print(data_extracted)
log_progress(f"Data successfully extracted")

#Fin de l'extraction
log_progress("Extract phase Ended") 

#Début de la transformation
log_progress("Transform phase Started") 

data_transformed = transform(data_extracted, "exchange_rate.csv")
print(data_transformed)
log_progress(f"Data successfully transformed")

#Fin de la transformation
log_progress("Transform phase Ended") 

# Début du chargement
log_progress("Load phase Started")

# Chargement CSV
log_progress("Load data to csv file Started")
load_to_csv(data_transformed, OUTPUT_PATH)
log_progress("Load data to csv file Ended")

# Chargement DB
sql_connection = sqlite3.connect(DB_NAME)   # Création de la connexion
log_progress("Load data to db Started")
load_to_db(data_transformed, sql_connection, TABLE_NAME)
log_progress("Load data to db Ended")

# Fin du chargement
log_progress("Load phase Ended")

# Requêtage
log_progress("SQL querying Started")
# Afficher toutes les banques
run_query("SELECT * FROM largest_banks", sql_connection)
# Calculer la moyenne de la capitalisation en GBP
run_query("SELECT AVG(MC_GBP_Billion) FROM largest_banks", sql_connection)
# Afficher les 5 premières banques
run_query("SELECT Name FROM largest_banks LIMIT 5", sql_connection)
log_progress("SQL querying Ended")

# Fermeture connexion
sql_connection.close()
# Fin du processus ETL
log_progress("ETL Job Ended")