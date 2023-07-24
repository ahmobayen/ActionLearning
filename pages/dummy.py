import streamlit as st
import requests

BASE_URL = "http://localhost:8000"  # Replace with your FastAPI server address


# def login_user(username, password):
#     data = {"username": username, "password": password}
#     return requests.post(f"{BASE_URL}/auth/login/", params=data)


# def login_main():
#     st.title("User Login")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if not username or not password:
#             st.error("Please enter both username and password.")
#         else:
#             response = login_user(username, password)
#             if response.status_code == 200:
#                 st.success("Login successful!")
#             else:
#                 st.error("Invalid credentials. Please try again.")

#     if st.button("Signup"):
#         st.write("[Signup for an account](http://localhost:8501/?page=registration)")



# Streamlit web application
def main():
    st.title("HOME")

    # Sidebar navigation
    page = st.sidebar.selectbox("Page", ["Sign up", "Login"])

    if page == "Sign up":
        signup_page()
    elif page == "Login":
        login_page()


def signup_page():
    st.header("Sign up")
    Fname = st.text_input("First Name")
    Lname = st.text_input("Last Name")
    email = st.text_input("Last Name")
    password = st.text_input("Last Name",type="password")
    DOB = st.date_input("DOB")

    if st.button("Sign up"):
        # Prepare data for prediction
        data = {
            "First name": Fname,
            "Last name": Lname,
            "DOB": DOB,
            "email": email,
            "password": password
        }

        # Make prediction API call
        response = requests.post(f"{BASE_URL}/Sign up", json=data)
        if response.status_code == 200:
            result = response.json()
            # prediction = "You have Heart Disease" if result["prediction"] == 1 else "You don't have Heart Disease"
            # st.success(f"Prediction: {prediction}")
            # st.success(f"Probability: {result['probability']}%")
        else:
            st.error("Signup failed.")

    # Upload CSV file for multiple predictions
   

def login_page():
    st.header("Sign up")
    email = st.text_input("Last Name")
    password = st.text_input("Last Name",type="password")
 

    if st.button("Sign up"):
        # Prepare data for prediction
        data = {
            "email": email,
            "password": password
     
        }

        # Make prediction API call
        response = requests.post(f"{BASE_URL}/Sign up", json=data)
        if response.status_code == 200:
            result = response.json()
            # prediction = "You have Heart Disease" if result["prediction"] == 1 else "You don't have Heart Disease"
            # st.success(f"Prediction: {prediction}")
            # st.success(f"Probability: {result['probability']}%")
        else:
            st.error("Signup failed.")



if __name__ == "__main__":
    main()