import streamlit as st

st.title(":red[Calculator]")
num1=st.number_input("enter number 1: ")
num2=st.number_input("enter number 2: ")
choice=st.selectbox("select your option",["add","sub","mult","div"])

if st.button("calculate"):
    if choice == "add":
        result = num1 + num2
        st.write(f"addition result{result}")
    elif choice == "sub":
        result = num1 - num2
        st.write(f"addition result{result}")
    elif choice == "mult":
        result = num1 * num2
        st.write(f"addition result{result}")
    elif choice == "div":
        result = num1 / num2
        st.write(f"addition result{result}")
