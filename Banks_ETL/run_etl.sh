#!/bin/bash
# run_etl.sh - Lance Banks_ETL avec téléchargement des taux de change

echo " Banks_ETL Pipeline "
date

# Naviguer vers le projet ou sortir si il n'existe pas
cd /mnt/c/Users/baaro/ETL_Projects/Banks_ETL || exit

# 1. Télécharger les taux de change
echo " Téléchargement des taux de change "
wget -q -O exchange_rate.csv \
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"

# Vérifier si le fichier est téléchargé pour continuer ou sinon sortir
if [ $? -eq 0 ]; then
    echo " Taux de change téléchargés "
else
    echo " Échec du téléchargement "
    exit 1
fi

# 2. Créer l'environnement virtuel si nécessaire
# Vérifier si l'environnement existe ou sinon le créer et continuer
if [ ! -d "venv" ]; then
    echo " Création de l'environnement virtuel "
    # Commande qui crée l'envirpnnement virtuel
    python3 -m venv venv
fi

# 3. Activer l'environnement
# Commande qui active l'environnement virtuel
source venv/bin/activate

# 4. Installer les dépendances
# Commande qui installe les bibliothèques requises
pip install -r requirements.txt -q

# 5. Lancer le script
echo " Lancement de Banks_ETL.py "
# Commande qui lance le script .py
python3 Banks_ETL.py

# 6. Désactiver l'environnement
# Commande qui désactive l'environnement virtuel
deactivate

echo " Banks_ETL terminé "
