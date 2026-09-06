# Importation des bibliothéques nécessaires
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime
import sqlite3

# Charge les variables d'environnement
load_dotenv()

# Les fichiers générés
LOG_FILE = "code_log.txt"
TABLE_NAME = "films" 
OUTPUT_PATH = "films.csv" 
DB_NAME = 'films.db'

#Ce script permet d'écrire des messages sur le fichier log et d'horodater
def log_progress(message): 
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format) 
    with open(LOG_FILE,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Fonction d'extraction des données de l'API
def extract(url, payload, headers):
    # Vérifier que la clé API est présente
    if not os.getenv("api_key"):
        raise ValueError("Clé API manquante. Vérifiez votre fichier .env")
    # Requête de l'API
    response = requests.post(url, data=payload, headers=headers)
    data = response.json()
    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Transformation du json en tableau
        df = pd.json_normalize(data["result"])
    else:
        raise ValueError("Erreur lors de l'extraction des données de l'API")
    return df

# Fonction de transformation des données extraites
def transform(df):
    # Sélection des données pertinentes et copie du dataframe
    df = df[["Series_Title", "Released_Year", "Runtime", "Genre", "IMDB_Rating",
             "Overview", "No_of_Votes", "Gross"]].copy()
    # Rennomage de colonnes
    df.columns = ["series_title", "released_year", "runtime_min", "genre", "rating",
                  "overview", "votes", "gross"]
    # Remplacer "min" et "," par espace ("")
    df["runtime_min"] = df["runtime_min"].str.replace("min", "")
    df["gross"] = df["gross"].str.replace(",", "")
    # Convertion de colonnes de type objet en string et gestion des valeurs nulles
    cols_str = ["series_title", "genre", "overview"]
    df[cols_str] = df[cols_str].astype("string").fillna("unknown")
    # Convertion de colonnes de type objet en entier et gestion des valeurs nulles
    cols_itg = ["runtime_min", "votes", "gross"]
    df[cols_itg] = df[cols_itg].apply(
        lambda col: pd.to_numeric(col, errors="coerce").fillna(0).astype(int)
    )
    # Convertion de colonne de type objet en float et gestion des valeurs nulles
    df["rating"] = df["rating"].fillna(0).astype(float)
    # Convertion de colonne de type objet en integer
    df["released_year"] = pd.to_numeric(df["released_year"], errors="coerce").astype("Int64")
    return df

# Fonction de chargement des données sous format csv
def load_to_csv(df, OUTPUT_PATH):
    # Chargement des données dans le fichier csv
    df.to_csv(OUTPUT_PATH, index = False)
    log_progress(f"Data successfully saved to csv at {OUTPUT_PATH}")

# Fonction de chargement des données dans une db
def load_to_db(df, conn, TABLE_NAME): 
    # Chargement des données dans la base de données
    df.to_sql(TABLE_NAME, conn, if_exists = 'replace', index = False)
    log_progress(f"Data successfully saved to database {DB_NAME} table {TABLE_NAME}")

# Fonction de requêtage sql
def run_query(query_statement, conn):
    """Exécute une requête SQL et affiche les résultats"""
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)
    log_progress(f"Query executed: {query_statement}")
    return query_output

#Début du processus ETL
log_progress("ETL Job Started") 

#Début de l'extraction
log_progress("Extract phase Started") 

url = "https://imdb-top-1000-movies-series.p.rapidapi.com/byrating"
payload = {
	"above": "0",
	"under": "10"
}
headers = {
	"x-rapidapi-key": os.getenv("api_key"),
	"x-rapidapi-host": "imdb-top-1000-movies-series.p.rapidapi.com",
	"Content-Type": "application/x-www-form-urlencoded"
}
data = extract(url, payload, headers)
print(data.head())
log_progress(f"Data successfully extracted")

#Fin de l'extraction
log_progress("Extract phase Ended") 

#Début de la transformation
log_progress("Transform phase Started") 

data_transformed = transform(data)
print(data_transformed.head())
log_progress(f"Data successfully transformed")

#Fin de la transformation
log_progress("Transform phase Ended") 

# Début du chargement
log_progress("Load phase Started")

# Chargement csv
log_progress("Load data to csv file Started")
load_to_csv(data_transformed, OUTPUT_PATH)
log_progress("Load data to csv file Ended")

# Chargement DB
conn = sqlite3.connect(DB_NAME)    # Création de la connexion
log_progress("Load data to db Started")
load_to_db(data_transformed, conn, TABLE_NAME)
log_progress("Load data to db Ended")

# Fin du chargement
log_progress("Load phase Ended")

# Requêtage
log_progress("SQL querying Started")
# Compter le nombre total de films
run_query("SELECT COUNT(*) FROM films", conn)
#  Afficher le top 50 des meilleurs films
run_query("SELECT Series_title, votes FROM films ORDER BY votes DESC LIMIT 50", conn)
# Calculer la moyenne des recettes du top 50
run_query("SELECT AVG(gross) AS avg_gross FROM films \
          WHERE series_title IN (SELECT Series_title FROM films ORDER BY votes DESC LIMIT 50)", conn)
#  Compter les films par genre dans le top 50
run_query("SELECT genre, COUNT(*) AS nb_films FROM films \
          WHERE Series_title IN (SELECT Series_title FROM films ORDER BY votes DESC LIMIT 50) \
          GROUP BY genre \
          ORDER BY nb_films DESC", conn)
log_progress("SQL querying Ended")

# Fermeture connexion
conn.close()
# Fin du processus ETL
log_progress("ETL Job Ended")