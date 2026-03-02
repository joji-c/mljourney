import streamlit as st
import joblib
st.title(":red[Grade Prediction]")
model = joblib.load("C:\\\\Users\\jojic\\OneDrive\\Desktop\\mljourney\\gui-building\\student_performance\\dt_model.pkl")
scaler = joblib.load("C:\\Users\\jojic\\OneDrive\\Desktop\\mljourney\\gui-building\\student_performance\\scaler.pkl")
StudyTimeWeekly = st.number_input("enter studytime")
Absences = st.number_input("enter absences")
Tutoring = st.number_input("enter tutoring")
ParentalSupport = st.number_input("enter ParentalSupport")
Extracurricular = st.number_input("enter Extracurricular")
if st.button("PREDICT GRADE"):
    test_data = [[StudyTimeWeekly,Absences,Tutoring,ParentalSupport,Extracurricular]]
    result = model.predict(scaler.transform(test_data))[0]
    grade_map = {0:"A",1:"B",2:"C",3:"D"}
    st.success(grade_map.get(result)) 

