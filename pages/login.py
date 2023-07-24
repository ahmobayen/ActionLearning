import streamlit as st
import requests

BASE_URL = "http://localhost:8000"  

def main():
    st.title("Welcome to stockmarket")

    page = st.sidebar.selectbox("Page", ["Sign up", "Login"])

    if page == "Sign up":
        signup_page()
    elif page == "Login":
        login_page()

def signup_page():
    st.header("Sign up")
    Fname = st.text_input("First Name")
    Lname = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    DOB = st.date_input("DOB")

    if st.button("Sign up"):
        data = {
            "First name": Fname,
            "Last name": Lname,
            "DOB": DOB,
            "email": email,
            "password": password
        }

        response = requests.post(f"{BASE_URL}/signup", json=data)
        if response.status_code == 200:
            result = response.json()
            if result["status"] == "user_exists":
                st.warning("User already exists. Please go to the Login page.")
                st.sidebar.selectbox("Page", ["Login"])
            else:
                st.success("Signup successful.")
        else:
            st.error("Signup failed.")

def login_page():
    st.header("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
 

    if st.button("Login"):
        # Prepare data for prediction
        data = {
            "email": email,
            "password": password
        }

        # Make prediction API call
        response = requests.post(f"{BASE_URL}/Login", json=data)
        if response.status_code == 200:
            result = response.json()
            # Handle the login response here (e.g., redirect to a new page or show a success message)
        else:
            st.error("Login failed.")

if __name__ == "__main__":
    main()
