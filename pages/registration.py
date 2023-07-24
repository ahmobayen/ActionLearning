# pages/registration.py

import streamlit as st
import requests

BASE_URL = "http://localhost:8000"  # Replace with your FastAPI server address


def register_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/auth/register/", json=data)
    return response.json()


def registration_main():
    st.title("Registration")
    reg_username = st.text_input("Username")
    reg_password = st.text_input("Password", type="password")
    if st.button("Register"):
        if reg_username and reg_password:
            response = register_user(reg_username, reg_password)
            st.success(f"Registered user: {response['username']}")

registration_main()