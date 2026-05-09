import numpy as np
import pandas as pd
import joblib

print("🚀 Prediction Started")

model = joblib.load("ipl_model.pkl")

df = pd.read_csv("cricket_data_2026.csv")
df = df.apply(pd.to_numeric, errors='coerce')
df.fillna(0, inplace=True)

features = [
    "Matches_Batted",
    "Runs_Scored",
    "Balls_Faced",
    "Fours",
    "Sixes",
    "Wickets_Taken",
    "Economy_Rate",
    "Bowling_Strike_Rate"
]

X = df[features]

# take one sample row
input_data = pd.DataFrame([X.iloc[0].values], columns=features)

prediction = model.predict(input_data)

print("🎯 Predicted Wickets:", prediction[0])