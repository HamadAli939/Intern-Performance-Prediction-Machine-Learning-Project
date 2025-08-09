import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved files
model = joblib.load("intern_performance_model.pkl")
scaler = joblib.load("intern_scaler.pkl")
dept_encoder = joblib.load("dept_encoder.pkl")
interact_encoder = joblib.load("interact_encoder.pkl")

st.set_page_config(page_title="Intern Performance Predictor", layout="centered")
st.title("🚀 Intern Performance Predictor")
st.markdown("Upload intern data to predict performance (Low / High).")

uploaded_file = st.file_uploader("Upload Excel or CSV file", type=["csv", "xls", "xlsx"])

if uploaded_file:
    # Determine file type and read accordingly
    if uploaded_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)

    # Encode categories
    df['department_encoded'] = dept_encoder.transform(df['department'])
    df['interaction_level_encoded'] = interact_encoder.transform(df['interaction_level'])

    # Feature columns
    features = [
        'attendance_rate',
        'task_completion_rate',
        'avg_feedback_score',
        'hours_per_week',
        'final_assessment_score',
        'department_encoded',
        'interaction_level_encoded's
    ]

    X = scaler.transform(df[features])
    preds = model.predict(X)

    df['Predicted Performance'] = np.where(preds == 1, 'High', 'Low')
    st.success("✅ Prediction complete!")
    st.dataframe(df[['intern_id', 'Predicted Performance']])

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Results", csv, "intern_predictions.csv", "text/csv")