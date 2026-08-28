# Multi_Sources_ETL - Multi-Format Data Processing

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org)

## Description

Pipeline ETL qui extrait des données depuis 3 formats différents (CSV, JSON, XML) contenus dans un fichier ZIP.
Transformations (conversion d'unités impériales en métriques) et chargement en CSV et SQLite.

## Technologies

- Python 3.8+
- Pandas 1.5+
- SQLite3

## Bibliothèques

- Pandas
- Requests

## Installation

pip install -r requirements.txt

## Utilisation

jupyter notebook Multi_Sources_ETL.ipynb

## Fichiers générés

- transformed_data.csv : Données transformées au format CSV
- cleaned_data.db : Base de données SQLite
- log_file.txt : Journal des opérations

## Structure du projet

Multi_Sources_ETL/
├── Multi_Sources_ETL.ipynb   # Notebook principal
├── README.md
├── requirements.txt
├── data/                     # Données sources (généré)
├── transformed_data.csv      # Résultat CSV (généré)
├── cleaned_data.db           # Base SQLite (générée)
└── log_file.txt              # Journal (généré)

## Exemple de résultat

Avant transformation :
    name  height  weight
0   alex   65.78  112.99

Après transformation :
    name  height  weight
0   alex    1.67   51.25

## Auteur

Arona Ba

- GitHub : https://github.com/baarona-98
- LinkedIn : https://linkedin.com/in/arona-ba-a440101b1