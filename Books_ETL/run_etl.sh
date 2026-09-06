#!/bin/bash
# run_etl.sh - Lance Books_ETL

echo " Books_ETL Pipeline "
date

# Naviguer vers le projet ou sortir si il n'existe pas
cd /mnt/c/Users/baaro/ETL_Projects/Books_ETL || exit

# Créer l'environnement virtuel si nécessaire
# Vérifier si l'environnement existe ou sinon le créer et continuer
if [ ! -d "venv" ]; then
    echo " Création de l'environnement virtuel "
    # Commande qui crée l'environnement virtuel
    python3 -m venv venv
fi

# Activer l'environnement
# Commande qui active l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
# Commande qui installe les bibliothèques requises
pip install -r requirements.txt -q

# Lancer le script
echo " Lancement de Books_ETL.py "
# Commande qui lance le script .py
python3 Books_ETL.py

# Désactiver l'environnement
# Commande qui désactive l'environnement virtuel
deactivate

echo " Books_ETL terminé "
