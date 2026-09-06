#!/bin/bash
# run_etl.sh - Lance Films_ETL (API nécessite .env)

echo " Films_ETL Pipeline "
date

# Naviguer vers le projet ou sortir si il n'existe pas
cd /mnt/c/Users/baaro/ETL_Projects/Films_ETL || exit

# 1. Vérifier que le fichier .env existe
# Vérifier que .env existe, si oui continuer ou sinon afficher un message et sortir 
if [ ! -f ".env" ]; then
    echo " Fichier .env manquant ! "
    echo " Créez un fichier .env avec votre clé API "
    exit 1
fi

# 2. Créer l'environnement virtuel si nécessaire
# Vérifier que l'environnement existe ou sinon le créer et continuer
if [ ! -d "venv" ]; then
    echo " Création de l'environnement virtuel "
    # Commande qui crée l'environnement virtuel
    python3 -m venv venv
fi

# 3. Activer l'environnement
# Commande qui active l'environnement virtuel
source venv/bin/activate

# 4. Installer les dépendances
# Commande qui installe les bibliothèques requises
pip install -r requirements.txt -q

# 5. Lancer le script
echo " Lancement de Films_ETL.py "
# Commande qui lance le script .py
python3 Films_ETL.py

# 6. Désactiver l'environnement
# Commande qui désactive l'environnement virtuel
deactivate

echo " Films_ETL terminé "
