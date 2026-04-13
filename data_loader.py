import pandas as pd

def load_data():
    df = pd.read_csv("water_potability.csv")
    
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    
    return df