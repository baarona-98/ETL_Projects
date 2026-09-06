# Importation des librairies nécessaires
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime

# Fichiers générés
LOG_FILE = "code_log.txt"
TABLE_NAME = "books" 
OUTPUT_PATH = "books.csv" 
DB_NAME = 'books.db'

#Ce script permet d'écrire des messages sur le fichier log et d'horodater
def log_progress(message): 
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format) 
    with open(LOG_FILE,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Fonction d'extraction des données
def extract(base_url):
    # Création d'un dataframe vide
    all_books = []    
    # Boucle pour extraire les données
    for page in range(1, 51):
        url = base_url.format(page)
        response = requests.get(url)
        # À ajouter dans Books_ETL et Banks_ETL
        if response.status_code != 200:
            raise ValueError(f"Erreur HTTP {response.status_code} sur {url}")
        else:
            response.encoding = "utf-8"   # force l'encodage correct
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find_all("article", class_="product_pod")
            for book in books:
                title = book.h3.a["title"]
                price = float(book.find("p", class_="price_color").text.replace("£", ""))
                availability = book.find("p", class_="instock availability").text.strip()
                rating = book.p["class"][1]  # ex: "Three", "Five"
                # Ajout des données extraites dans le dataframe vide
                all_books.append({
                    "title": title,
                    "price": price,
                    "availability": availability,
                    "rating": rating
                })
    # Transformation en DataFrame
    df = pd.DataFrame(all_books)
    return df

# Fonction de transformation des données
def transform(df, csv_path):
    # Création d'une copie des données extraites
    df = df.copy() 
    # Transformation de nombre de lettre en chiffre
    rating_map = {"One": 1,"Two": 2,"Three": 3,"Four": 4,"Five": 5}
    df["rating"] = df["rating"].map(rating_map).astype(int)
    # Rennomage de colonnes
    df = df.rename(columns = {"price": "price_GBP"})
    # Extraction des données du fichier csv
    df1 = pd.read_csv(csv_path, sep = ";")
    # Transformation en dictionnaire clé/valeur
    rates = df1.set_index("Currency")["Rate"].to_dict()
    # Ajout de colonnes et convertion
    df["price_EUR"] = (df["price_GBP"] * rates["EUR"]).round(2)
    df["price_USD"] = (df["price_GBP"] * rates["USD"]).round(2)
    df["price_INR"] = (df["price_GBP"] * rates["INR"]).round(2)
    # Convertion de colonne de type object en string
    cols_str = ["title", "availability"]
    df[cols_str] = df[cols_str].astype("string")
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
    # Exécute une requête SQL et affiche les résultats
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)
    log_progress(f"Query executed: {query_statement}")
    return query_output

#Début du processus ETL
log_progress("ETL Job Started") 

#Début de l'extraction
log_progress("Extract phase Started") 

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
data = extract(base_url)
print(data.head())
log_progress(f"Data successfully extracted")

#Fin de l'extraction
log_progress("Extract phase Ended") 

#Début de la transformation
log_progress("Transform phase Started") 

data_transformed = transform(data, "exchange_rate.csv")
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
# Compter le nombre total de livres
run_query("SELECT COUNT(*) FROM books", conn)
# Compter les livres en stock
run_query("SELECT COUNT(title) FROM books WHERE availability = 'In stock'", conn)
# Compter les livres par note
run_query("SELECT COUNT(title), rating FROM books GROUP BY rating", conn)
log_progress("SQL querying Ended")

# Fermeture de la connexion
conn.close()
# Fin du processus ETL
log_progress("ETL Job Ended")