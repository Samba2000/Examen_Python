import pandas as pd

def load_data():
    """Charge et nettoie le jeu de données Ames Housing."""
    df = pd.read_csv("data/AmesHousing.csv")

    # Sélection des colonnes clés
    selected_columns = ["SalePrice", "Gr Liv Area", "Year Built", "Neighborhood", "Lot Area"]
    df = df[selected_columns].dropna()

    # Statistiques descriptives
    stats = df.describe()

    return df, stats
