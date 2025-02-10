import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def show_visualizations(df):
    
    st.subheader("Distribution des Prix")
    fig, ax = plt.subplots()
    sns.histplot(df["SalePrice"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    # Répartition des ventes par quartier
    df_counts = df["Neighborhood"].value_counts().reset_index()
    df_counts.columns = ["Neighborhood", "PrixVendu"]

    st.subheader("Répartition des ventes par quartier")
    fig = px.bar(df_counts, x="Neighborhood", y="PrixVendu", labels={"Neighborhood": "Quartier", "PrixVendu": "Nombre de ventes"})
    st.plotly_chart(fig)

    st.subheader("Relation entre la surface et le prix")
    fig = px.scatter(df, x="Gr Liv Area", y="SalePrice", color="Neighborhood", title="Surface habitable vs Prix", opacity=0.7)
    st.plotly_chart(fig)

    if "Latitude" in df.columns and "Longitude" in df.columns:
        st.subheader("Carte de densité des ventes")
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="SalePrice", size="Gr Liv Area",
                                color_continuous_scale="Viridis", zoom=10, mapbox_style="open-street-map")
        st.plotly_chart(fig)

 
    df_numeric = df.select_dtypes(include=["number"]) 
    corr_matrix = df_numeric.corr()

    st.subheader("Corrélations entre variables")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)
