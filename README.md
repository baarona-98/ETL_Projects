# Portfolio ETL - Projets de Data Engineering

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org)
[![ETL](https://img.shields.io/badge/Type-ETL-brightgreen.svg)]()
[![Status](https://img.shields.io/badge/Status-Terminé-brightgreen.svg)]()

## 🎓 À propos

Ce dépôt regroupe **4 projets ETL** (Extract, Transform, Load) réalisés dans le cadre de ma formation **Data Engineering** (certification IBM).

Chaque projet explore une source de données différente :
- **Web Scraping** (Wikipedia, Books)
- **API REST** (IMDb)
- **Fichiers multi-formats** (CSV, JSON, XML)

---

## 🤖 Utilisation de l'IA

Ces projets ont été réalisés avec l'assistance d'outils d'**intelligence artificielle** (notamment pour l'optimisation du code, le debugging et l'amélioration des bonnes pratiques).  
L'objectif est de démontrer ma capacité à :
- **Comprendre et adapter** du code assisté par IA
- **Appliquer** des concepts de Data Engineering
- **Construire** des pipelines ETL fonctionnels
- **Documenter** et **structurer** des projets professionnels

*Tous les projets restent le fruit de ma compréhension et de mon apprentissage.*

---

## 📋 Projets

### 1. 🏦 Banks_ETL - Web Scraping
- **Source** : Wikipedia
- **Objectif** : Extraire les 10 plus grandes banques du monde, convertir leurs capitaux dans différentes devises (EUR, GBP, INR), et charger en CSV et SQLite.
- **Technologies** : Python, BeautifulSoup4, Pandas, SQLite3
- 🔗 [Voir le projet](Banks_ETL/)

---

### 2. 📚 Books_ETL - Web Scraping
- **Source** : books.toscrape.com
- **Objectif** : Récupérer 1000 livres (50 pages × 20 livres), enrichir les données avec des taux de change (EUR, USD, INR), et charger en CSV et SQLite.
- **Technologies** : Python, BeautifulSoup4, Pandas, SQLite3
- 🔗 [Voir le projet](Books_ETL/)

---

### 3. 🎬 Films_ETL - API
- **Source** : API IMDb (via RapidAPI)
- **Objectif** : Récupérer les 1000 meilleurs films, transformer les données (nettoyage), et charger en CSV et SQLite.
- **Technologies** : Python, Requests, Pandas, SQLite3
- 🔗 [Voir le projet](Films_ETL/)

---

### 4. 📊 Multi_Sources_ETL - Multi-Format Data Processing
- **Source** : Fichier ZIP contenant des données CSV, JSON et XML
- **Objectif** : Extraire et consolider des données depuis 3 formats différents, les transformer (conversion d'unités impériales en métriques), et charger en CSV et SQLite.
- **Technologies** : Python, Pandas, SQLite3
- 🔗 [Voir le projet](Multi_Sources_ETL/)

---

## 🛠️ Compétences développées

| Compétence | Détail |
|------------|--------|
| **Web Scraping** | BeautifulSoup, Requests |
| **API REST** | Appels API, gestion de clés (.env) |
| **Manipulation de données** | Pandas (DataFrames) |
| **Bases de données** | SQLite3 |
| **Formats de fichiers** | CSV, JSON, XML |
| **ETL** | Pipelines complets Extract → Transform → Load |
| **Journalisation** | Logging avec timestamps |
| **IA Assistée** | Optimisation du code, debugging, bonnes pratiques |

---

## 🚀 Comment exécuter les projets

Chaque projet est un notebook Jupyter :

```bash
# 1. Naviguer dans un projet
cd Banks_ETL

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le notebook
jupyter notebook Banks_ETL.ipynb


## Auteur

Arona Ba

GitHub : https://github.com/baarona-98
LinkedIn : https://linkedin.com/in/arona-ba-a440101b1

Projets realises dans le cadre de la certification IBM Data Engineering.