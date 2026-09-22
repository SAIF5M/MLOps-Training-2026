import pandas as pd
from src.config_loader import load_config
from src.preprocessing import preprocess_data

def make_prediction(input_data: dict):
    
    config = load_config()
    
    df = pd.DataFrame([input_data])
    
    processed_df = preprocess_data(df)
    
    
    prediction = 0
    probability = 0.15
    
    return {
        "prediction": int(prediction),
        "probability": float(probability),
        "model_version": config["model"]["version"]
    }