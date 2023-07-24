# pages/login.py

import streamlit as st
import requests

BASE_URL = "http://localhost:8000"  # Replace with your FastAPI server address


def login_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/auth/login/", json=data)
    return response.json()


def login_main():
    st.title("Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_username and login_password:
            response = login_user(login_username, login_password)
            st.success(response["message"])

login_main()