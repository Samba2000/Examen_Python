import streamlit as st
from src.chargement import load_data
from src.filtre import apply_filters
from src.visualisation import show_visualizations
from src.analyse import show_analytics

st.set_page_config(page_title="Dashboard des Données Ames Housing ", layout="wide")

# Introduction
st.title("Dashboard des Données Ames Housing ")
st.write("Explorez et analysez les prix de l'immobilier à Ames avec des visualisations interactives.")

# Charger les données
df, stats = load_data()

# Affichage des données
st.subheader("Aperçu des données")
st.dataframe(df.head())

# Affichage des statistiques
st.subheader("Statistiques descriptives")
st.dataframe(stats)

# Filtres interactifs
filtered_df = apply_filters(df)

# Visualisations des données
show_visualizations(filtered_df)

# Afficher l'analyse avancée
show_analytics(filtered_df)
