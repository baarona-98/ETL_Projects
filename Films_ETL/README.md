# Films_ETL - API IMDb

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![REST API](https://img.shields.io/badge/REST-API-purple.svg)](https://rapidapi.com)

## Configuration requise

Avant d'exécuter ce projet, vous devez obtenir une clé API !

1. Créez un compte sur RapidAPI (https://rapidapi.com/)
2. Abonnez-vous à l'API "IMDb Top 1000 Movies & Series"
3. Récupérez votre clé API
4. Créez un fichier .env :

api_key=votre_cle_api_rapidapi_ici

## Description

Récupération des 1000 meilleurs films depuis l'API IMDb (via RapidAPI).
Transformations (nettoyage des données) et chargement en CSV et SQLite.

Données extraites par film :
- Titre
- Année de sortie
- Durée (minutes)
- Genre
- Note IMDb
- Synopsis
- Nombre de votes
- Recettes

## Technologies

- Python 3.8+
- Requests 2.28+
- Pandas 1.5+
- python-dotenv 0.20+
- SQLite3

## Bibliothèques

- Requests
- Pandas
- python-dotenv

## Installation

pip install -r requirements.txt
cp .env.example .env

## Utilisation

jupyter notebook Films_ETL.ipynb

## Fichiers générés

- films.csv : Données des films transformées
- films.db : Base de données SQLite
- code_log.txt : Journal des opérations

## Structure du projet

Films_ETL/
├── Films_ETL.ipynb           # Notebook principal
├── README.md
├── requirements.txt
├── .env                       # Variables d'environnement (à créer)
├── .env.example               # Exemple de configuration
├── films.csv                  # Résultat CSV (généré)
├── films.db                   # Base SQLite (générée)
└── code_log.txt               # Journal (généré)

## Source des données

API : IMDb Top 1000 Movies & Series via RapidAPI
Endpoint : https://imdb-top-1000-movies-series.p.rapidapi.com/byrating

## Exemple de résultat

The Shawshank Redemption : 1994 - 142 min - Note 9.3 - 2 343 110 votes
The Godfather : 1972 - 175 min - Note 9.2 - 1 620 367 votes

## Auteur

Arona Ba

- GitHub : https://github.com/baarona-98
- LinkedIn : https://linkedin.com/in/arona-ba-a440101b1