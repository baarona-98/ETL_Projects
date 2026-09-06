# Chargement des librairies nécessaires
import requests, zipfile, io
import glob 
import pandas as pd
import xml.etree.ElementTree as ET  
from datetime import datetime
import sqlite3

# Fichiers générés
LOG_FILE = "log_file.txt"
TARGET_FILE = "transformed_data.csv"
DB_NAME = "cleaned_data.db"
TABLE_NAME = "transformed_data"

#Ce script permet d'écrire des messages sur le fichier log et d'horodater
def log_progress(message): 
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format) 
    with open(LOG_FILE,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Fonction d'extraction de fichier csv
def extract_from_csv(file_to_process): 
    df = pd.read_csv(file_to_process)
    return df
# Fonction d'extraction de fichier json
def extract_from_json(file_to_process):
    df = pd.read_json(file_to_process, lines=True)
    return df 
# Fonction d'extraction de fichier xml (CORRIGÉE - plus de warnings)
def extract_from_xml(file_to_process):  
    # Extraction des données
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    # Collecte des données dans une liste
    data = []
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        data.append({"name": name, "height": height, "weight": weight})
    # Création du DataFrame à partir de la liste
    df = pd.DataFrame(data)
    return df

# Cette fonction permet d'assembler tous les données extraites
def extract(): 
    # Liste pour collecter tous les DataFrames
    dfs = []
    # Extraction CSV
    for csvfile in glob.glob("data/*.csv"): 
        if csvfile != TARGET_FILE: 
            df = extract_from_csv(csvfile)
            dfs.append(df)
    # Extraction JSON
    for jsonfile in glob.glob("data/*.json"): 
        df = extract_from_json(jsonfile)
        dfs.append(df)
    # Extraction XML
    for xmlfile in glob.glob("data/*.xml"): 
        df = extract_from_xml(xmlfile)
        dfs.append(df)
    # Concaténation unique
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
        return df
    else:
        df = pd.DataFrame(columns=['name','height','weight'])
        return df

#Ce script transforme les données extraites
def transform(df): 
    '''Convertir les pouces en mètres et arrondir à deux décimales
    1 pouce = 0.0254 mètres'''
    df['height'] = round(df.height * 0.0254,2) 
    '''Convertir les livres en kilogrammes et arrondir à deux décimales
    1 livre = 0.45359237 kilogrammes'''
    df['weight'] = round(df.weight * 0.45359237,2)
    # Convertion de colonnes de type objet en string
    df["name"] = df["name"].astype("string")
    # Suppression des doublons et réinitialisation de l'index
    df = df.drop_duplicates().reset_index(drop=True)
    return df 

# Fonction de chargement des données sous format csv
def load_to_csv(df, TARGET_FILE):
    # Chargement des données dans le fichier csv
    df.to_csv(TARGET_FILE, index=False)
    log_progress(f"Data successfully saved to csv at {TARGET_FILE}")
    
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

# Début du processus ETL
log_progress("ETL Job Started") 
 
# Début de l'extraction
log_progress("Extract phase Started") 

extracted_data = extract() 
print(extracted_data)
log_progress("Data successfully extracted")
 
# Fin de l'extraction
log_progress("Extract phase Ended")

#Début de la transformation
log_progress("Transform phase Started") 

transformed_data = transform(extracted_data) 
print(transformed_data) 
log_progress(f"Data successfully transformed")
 
#Fin de la transformation
log_progress("Transform phase Ended") 

# Début du chargement
log_progress("Load phase Started")

# Chargement CSV
log_progress("Load data to csv file Started")
load_to_csv(transformed_data, TARGET_FILE)
log_progress("Load data to csv file Ended")

# Chargement DB
sql_connection = sqlite3.connect(DB_NAME)   # Création de la connexion
log_progress("Load data to db Started")
load_to_db(transformed_data, sql_connection, TABLE_NAME)
log_progress("Load data to db Ended")

# Fin du chargement
log_progress("Load phase Ended")

# Requêtage
log_progress("SQL querying Started")
# Afficher toutes les lignes
run_query("SELECT * FROM transformed_data", sql_connection)
# Affiche le nom et la taille du plus lourd
run_query("SELECT name, height FROM transformed_data \
          WHERE weight = (SELECT max(weight) FROM transformed_data)", sql_connection)
# Afficher les 3 plus lourd
run_query("SELECT name, weight FROM transformed_data ORDER BY weight DESC LIMIT 3", sql_connection)
log_progress("SQL querying Ended")

# Fermeture connexion
sql_connection.close()
# Fin du processus ETL
log_progress("ETL Job Ended")