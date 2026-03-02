import streamlit as st
import joblib

st.title(":red[Drug type predictor:]")

model = joblib.load("dt_model.pkl")
scaler = joblib.load("scaler.pkl")

Age = st.number_input("Enter Age", min_value=0)
Male = st.number_input("Enter 1 if Male")
Female = st.number_input("Enter 1 if Female")
Low_Bp= st.number_input("Enter 1 if Low_Bp")
Normal_Bp= st.number_input("Enter 1 if Normal_Bp")
High_Bp= st.number_input("Enter 1 if High_Bp")
Normal_Colestrol= st.number_input("Enter 1 if Normal_Colestrol")
High_cholestrol= st.number_input("Enter 1 if High_colestrol")
Na = st.number_input("Enter Sodium to Potassium level")

if st.button("Predict Drug Type"):
    test_data = [[Age,Male,Female,Low_Bp,Normal_Bp,High_Bp,Normal_Colestrol,High_cholestrol,Na]]
    result = model.predict(scaler.transform(test_data))[0]
    grade_map = { 0:'drugY', 1:'drugC', 2:'drugX', 3:'drugA', 4:'drugB'}
    st.success(f"Predicted Drug: {grade_map[result]}")
