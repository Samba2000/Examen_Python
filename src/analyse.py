import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def show_analytics(df):
    
    st.subheader("Prédiction du Prix en fonction des Caractéristiques")

    features = st.multiselect("Sélectionnez les variables pour la prédiction", 
                              ["Gr Liv Area", "Year Built", "Lot Area"], 
                              default=["Gr Liv Area"])
    
    if not features:
        st.warning("Veuillez sélectionner au moins une variable pour la prédiction.")
        return

    # Modèle de régression linéaire
    X = df[features]
    y = df["SalePrice"]

    # Séparation des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prédictions
    y_pred = model.predict(X_test)
    df_pred = X_test.copy()
    df_pred["Actual Price"] = y_test
    df_pred["Predicted Price"] = y_pred

    # Graphique : Prix réel vs Prix prédit
    st.subheader("Comparaison des Prix réels et prédits")
    fig = px.scatter(df_pred, x="Actual Price", y="Predicted Price", title="Prix Réel vs Prix Prédit",
                     labels={"Actual Price": "Prix réel", "Predicted Price": "Prix prédit"})
    fig.add_shape(type="line", x0=df["SalePrice"].min(), y0=df["SalePrice"].min(),
                  x1=df["SalePrice"].max(), y1=df["SalePrice"].max(), line=dict(color="red", dash="dash"))
    st.plotly_chart(fig)

    # Statistiques du modèle
    r2 = r2_score(y_test, y_pred)
    st.write(f"Coefficient de détermination (R²) : {r2:.4f}")
    for feature, coef in zip(features, model.coef_):
        st.write(f"Effet de {feature} sur le Prix : {coef:.2f}")

    # Analyse des facteurs influents avec un modèle Random Forest
    st.subheader("Importance des variables dans la prédiction")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    feature_importances = pd.DataFrame({"Feature": features, "Importance": rf_model.feature_importances_})
    feature_importances = feature_importances.sort_values(by="Importance", ascending=False)

    fig = px.bar(feature_importances, x="Feature", y="Importance", title="Importance des Variables")
    st.plotly_chart(fig)
