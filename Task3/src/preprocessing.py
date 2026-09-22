import pandas as pd
import joblib
from pathlib import Path
from src.config_loader import load_config

def load_fitted_objects():
    config = load_config()
    models_path = Path(__file__).resolve().parent.parent / config["paths"]["models_path"]
    
    return models_path

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
  
    processed_df = df.copy()
    
    
    return processed_df