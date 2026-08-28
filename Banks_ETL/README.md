# Banks_ETL - Web Scraping Wikipedia

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-4.11+-green.svg)](https://www.crummy.com/software/BeautifulSoup/)

## Description

Extraction des 10 plus grandes banques du monde depuis Wikipedia via web scraping.
Transformation et enrichissement avec un fichier CSV de taux de change (EUR, GBP, INR).
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

## Installation

pip install -r requirements.txt

## Utilisation

jupyter notebook Banks_ETL.ipynb

## Fichiers générés

- largest_banks_data.csv : Données des banques enrichies
- banks.db : Base de données SQLite
- code_log.txt : Journal des opérations

## Structure du projet

Banks_ETL/
├── Banks_ETL.ipynb           # Notebook principal
├── README.md
├── requirements.txt
├── exchange_rate.csv         # Taux de change (téléchargé)
├── largest_banks_data.csv    # Résultat CSV (généré)
├── banks.db                  # Base SQLite (générée)
└── code_log.txt              # Journal (généré)

## Source des données

Wikipedia : https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks

## Exemple de résultat

JPMorgan Chase : 432.92 USD / 402.62 EUR / 346.34 GBP / 35910.71 INR
Bank of America : 231.52 USD / 215.31 EUR / 185.22 GBP / 19204.58 INR

## Auteur

Arona Ba

- GitHub : https://github.com/baarona-98
- LinkedIn : https://linkedin.com/in/arona-ba-a440101b1