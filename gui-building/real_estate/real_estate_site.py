import streamlit as st
import joblib
st.title(":red[Real Estate Prediction :]")
model=joblib.load("C:\\Users\\jojic\\OneDrive\\Desktop\\mljourney\\gui-building\\real_estate\\dt_model.pkl")
scaler=joblib.load("C:\\Users\\jojic\\OneDrive\\Desktop\\mljourney\\gui-building\\real_estate\\scaler.pkl")
house_age=st.number_input("enter house age")
distance_to_station=st.number_input("enter distance to station")
number_of_stores=st.number_input("enter number of stores near")
latitude=st.number_input("enter latitude")
longitude=st.number_input("enter longitude")
if st.button("PREDICT HOUSE PRICE"):
    test_data=[[house_age,distance_to_station,number_of_stores,latitude,longitude]]
    result = model.predict(scaler.transform(test_data))
    st.success(result)