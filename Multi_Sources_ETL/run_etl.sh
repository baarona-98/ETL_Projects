#!/bin/bash
# run_etl.sh - Lance M_S_ETL avec téléchargement des données

echo " M_S_ETL Pipeline "
date

# Naviguer vers le projet ou sortir si il n'existe pas
cd /mnt/c/Users/baaro/ETL_Projects/Multi_Sources_ETL || exit

# 1. Télécharger le fichier source
echo " Téléchargement des données sources "
wget -q -O source.zip \
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip"

# Vérifier si le fichier est téléchargé pour continuer ou sinon sortir
if [ $? -eq 0 ]; then
    echo " Source.zip téléchargé "
else
    echo " Echec du téléchargement "
    exit 1
fi

# 2. Extraire les données
echo " Extraction des données "
# Créer un dossier data/
mkdir -p data
# Dézipper le fichier zip dans le dossier data/
unzip -o -q source.zip -d data/ 
# Supprimer le fichier zip
rm source.zip
echo " Données extraites dans data/ "

# 3. Créer l'environnement virtuel si nécessaire
# Vérifier si l'environnement existe ou sinon le créer et continuer
if [ ! -d "venv" ]; then
    echo " Création de l'environnement virtuel "
    # Commande qui crée l'environnement virtuel
    python3 -m venv venv
fi

# 4. Activer l'environnement
# Commande qui active l'environnement virtuel
source venv/bin/activate

# 5. Installer les dépendances
# Commande qui installe les bibliothèques requises
pip install -r requirements.txt -q

# 6. Lancer le script
echo " Lancement de M_S_ETL.py "
# Commande qui lance le script .py
python3 M_S_ETL.py

# 7. Désactiver l'environnement
# Commande qui désactive l'environnement virtuel
deactivate

echo " M_S_ETL terminé "
