# Books_ETL - Web Scraping

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-4.11+-green.svg)](https://www.crummy.com/software/BeautifulSoup/)

## Description

Récupération de 1000 livres (50 pages × 20 livres) depuis books.toscrape.com via web scraping.
Transformation et enrichissement avec un fichier CSV de taux de change (EUR, USD, INR).
Chargement en CSV et SQLite.

## Technologies

- Python 3.8+
- BeautifulSoup4 4.11+
- Pandas 1.5+
- SQLite3

## Bibliothèques

- Requests
- BeautifulSoup4
- Pandas

## Utilisation

# Rendre le fichier run_etl.sh exécutable
chmod +x run_etl.sh

# Lancer le pipeline
./run_etl.sh


Le script `run_etl.sh` gère automatiquement :

- La création et l'activation de l'environnement virtuel
- L'installation des dépendances
- L'exécution du pipeline
- La désactivation de l'environnement


## Fichiers générés

- books.csv : Données des livres enrichies
- books.db : Base de données SQLite
- code_log.txt : Journal des opérations

## Structure du projet

Books_ETL/
├── Books_ETL.py          # Script ETL principal
├── run_etl.sh            # Script Shell (lancement)
├── README.md             # Documentation
├── requirements.txt      # Dépendances Python
├── venv/                 # Environnement virtuel (créé automatiquement)
├── exchange_rate.csv     # Taux de change (Déjà téléchargé)
├── books.csv             # Résultat CSV (généré)
├── books.db              # Base SQLite (générée)
└── code_log.txt          # Journal (généré)

## Source des données

Site web : https://books.toscrape.com/
Pages : 50 pages × 20 livres = 1000 livres

## Exemple de résultat

A Light in the Attic : 51.77 GBP / 59.54 EUR / 67.30 USD / 5368.03 INR - Note 3/5
Tipping the Velvet : 53.74 GBP / 61.80 EUR / 69.86 USD / 5572.30 INR - Note 1/5

## Auteur

Arona Ba

- GitHub : https://github.com/baarona-98
- LinkedIn : https://linkedin.com/in/arona-ba-a440101b1