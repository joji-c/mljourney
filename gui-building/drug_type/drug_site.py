import streamlit as st
import joblib

st.title(":red[Drug type predictor:]")

model = joblib.load("dt_model.pkl")
scaler = joblib.load("scaler.pkl")

Age = st.number_input("Enter Age", min_value=0)
Sex = st.selectbox("Select Sex", ["M", "F"])
BP = st.selectbox("Select BP", ["LOW", "NORMAL", "HIGH"])
Cholesterol = st.selectbox("Select Cholesterol", ["NORMAL", "HIGH"])
Na = st.number_input("Enter Sodium to Potassium level")

if st.button("Predict Drug Type"):
    sex_map = {'M': 0, 'F': 1}
    bp_map = {'LOW': 0, 'NORMAL': 1, 'HIGH': 2}
    chol_map = {'NORMAL': 0, 'HIGH': 1}
    test_data = [[Age,sex_map[Sex],bp_map[BP],chol_map[Cholesterol],Na]]
    result = model.predict(scaler.transform(test_data))[0]
    grade_map = { 0:'drugY', 1:'drugC', 2:'drugX', 3:'drugA', 4:'drugB'}
    st.success(f"Predicted Drug: {grade_map[result]}")