import streamlit as st
num1=st.number_input("enter number 1: ")
num2=st.number_input("enter number 2: ")

if st.button("Add"):
    sum = num1 + num2
    st.write(f"addition result{sum}")

if st.button("Subtraction"):
    diff = num1 - num2
    st.write(f"addition result{diff}")

