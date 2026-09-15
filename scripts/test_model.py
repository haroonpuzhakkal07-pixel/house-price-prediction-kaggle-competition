import sys
from pathlib import Path

import pandas as pd
import joblib

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


MODEL_PATH = PROJECT_ROOT / "artifacts" / "house_price_model.joblib"
TEST_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "train.csv"


# Load the saved model
model = joblib.load(MODEL_PATH)

print("Model loaded successfully.")


# Load one real property from the training data
train = pd.read_csv(TEST_DATA_PATH)

sample = train.drop(columns=["SalePrice"]).iloc[[0]]


# Predict
prediction = model.predict(sample)[0]


print(f"Predicted SalePrice: ${prediction:,.2f}")