import streamlit as st
import joblib

st.title(":red[Drug type predictor:]")

model = joblib.load("dt_model.pkl")
scaler = joblib.load("scaler.pkl")

Age = st.slider("select age",1,100)
Gender=st.selectbox("select Gender",["Male","Female"])
Bp=st.selectbox("select Blood Preasure level",["High","Normal","Low"])
Cholestrol=st.selectbox("select Cholestrol level",["High","Normal"])
Na = st.number_input("Enter Sodium to Potassium level")

if st.button("Predict Drug Type"):
    gender_map = {"Male":0, "Female":1}
    bp_map = {"High":0, "Normal":1, "Low":2}
    chol_map = {"High":0, "Normal":1}
    test_data = [[Age,gender_map[Gender],bp_map[Bp],chol_map[Cholestrol],Na]]
    result = model.predict(scaler.transform(test_data))[0]
    grade_map = { 0:'DrugY', 1:'DrugC', 2:'DrugX', 3:'DrugA', 4:'DrugB'}
    st.success(f"Drug Type : {grade_map[result]}")

