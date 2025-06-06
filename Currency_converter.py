
#importing necessary libraries 
import streamlit as st
import requests

#Set title
st.title("Live :rainbow[Currency] Converter")

#Taking inputs fro user
amount = st.number_input("Enter the amount in INR: ", 1)
target_curr = st.selectbox("Convert to: ", ["USD", "JPY","EUR"])

#fetching and displaying data
if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_curr]
        converted = amount* rate
        st.success(f"{amount} INR= {converted} {target_curr}")
    else:
        st.error("Some Error Occured")
