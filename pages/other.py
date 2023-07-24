import streamlit as st
import requests
import pandas as pd
def main():
    st.title("Stock Market App")
    
    

    

    
    # Add user authentication logic here (signup, login, etc.)
    
    page = st.sidebar.selectbox("Page", ["Sign Up", "Login","Stock List", "Manage Stocks", "Notifications", "Stock Details", "Stock Comparison"])

    if page == "Sign Up":
        signup_page()
    elif page == "Login":
        login_page()
    if page == "Stock List":
        stock_list_page()
    elif page == "Manage Stocks":
        manage_stocks_page()
    elif page == "Notifications":
        notifications_page()
    elif page == "Stock Details":
        stock_details_page()
    elif page == "Stock Comparison":
        stock_comparison_page()


def signup_page():
    st.header("Sign Up")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    dob = st.date_input("Date of Birth")

    if st.button("Sign Up"):
        # Implement the backend API call to register the user
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "dob": str(dob),
        }
        response = requests.post("http://localhost:8000/signup", json=data)
        if response.status_code == 200:
            result = response.json()
            st.success("Sign up successful. Please proceed to login.")
        else:
            st.error("Sign up failed. Please try again.")

def login_page():
    st.header("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Implement the backend API call for user authentication
        data = {
            "email": email,
            "password": password,
        }
        response = requests.post("http://localhost:8000/login", json=data)
        if response.status_code == 200:
            result = response.json()
            # Redirect to the user's dashboard or another page on successful login
            st.success("Login successful.")
            st.info("Redirecting to your dashboard...")
            # Optionally, you can add more logic here, like setting a user session.
        else:
            st.error("Login failed. Please check your credentials.")


if __name__ == "__main__":
    main()
