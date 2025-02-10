import streamlit as st

def apply_filters(df):
    # Filtre par prix avec un slider
    prix_min, prix_max = int(df["SalePrice"].min()), int(df["SalePrice"].max())
    prix_range = st.sidebar.slider("Filtrer par prix", prix_min, prix_max, (prix_min, prix_max))

    # Filtre par quartier (Neighborhood)
    neighborhoods = st.sidebar.multiselect("Sélectionner un quartier", df["Neighborhood"].unique(), default=df["Neighborhood"].unique())

    # Filtre par année de construction
    annee_min, annee_max = int(df["Year Built"].min()), int(df["Year Built"].max())
    annee_range = st.sidebar.slider("Année de construction", annee_min, annee_max, (annee_min, annee_max))

    # Filtrage des données
    df_filtered = df[
        (df["SalePrice"] >= prix_range[0]) & (df["SalePrice"] <= prix_range[1]) &
        (df["Year Built"] >= annee_range[0]) & (df["Year Built"] <= annee_range[1]) &
        (df["Neighborhood"].isin(neighborhoods))
    ]

    return df_filtered
