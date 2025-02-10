Dashboard des Données Ames Housing 

1. Description

L'application Ames Housing Dashboard permet d'explorer et d'analyser les prix de l'immobilier à Ames grâce à des visualisations interactives et une analyse avancée des données.

2. Fonctionnalités principales
Chargement et nettoyage des données
-> Suppression des valeurs manquantes.
-> Sélection des colonnes clés pour l'analyse.

Exploration et visualisation des données
-> Histogramme de la répartition des prix.
-> Graphique en barres des ventes par quartier.
-> Carte interactive pour visualiser la densité des ventes.
-> Heatmap des corrélations entre les variables.

Filtres interactifs
-> Filtrer les données par plage de prix.
-> Sélectionner des catégories (quartier, année de construction, etc.).
-> Appliquer plusieurs filtres en simultané.

Analyse avancée et prédiction des prix
-> Modèle de régression linéaire pour prédire les prix en fonction de la surface et d'autres caractéristiques.
-> Évaluation du modèle.
-> Identification des facteurs influents.

3. Installation et Exécution

Prérequis
-> Avant de commencer, assure-toi d'avoir Python 3.8+ installé sur ta machine.

Cloner le projet
-> git clone https://github.com/Samba2000/Examen_Python.git
-> cd Examen_Python

Installer les dépendances
-> Utilise pip pour installer les bibliothèques nécessaires :
    streamlit
    pandas
    matplotlib
    seaborn
    scikit-learn
    plotly

Exécuter l'application Streamlit
-> streamlit run app.py

Structure du projet

Examen/
│── data/   # Dossier contenant le dataset (AmesHousing.csv)
│── app.py  # Fichier principal de l'application
│── src/chargement.py        # Chargement des données
│── src/analyse.py           # Analyse avancée et prédiction des prix
│── src/visualisation.py     # Visualisations et graphiques interactifs
│── src/filtre.py            # Gestion des filtres interactifs
│── requirements.txt         # Liste des dépendances Python
│── README.md                # Documentation du projet


Auteurs
👨‍💻 Samba DRAME
📧 Email : dramembasa2000@gmail.com
Projet réalisé dans le cadre du cours de Python Analyse des données