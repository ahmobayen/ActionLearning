import requests

url = "http://127.0.0.1:8000/auth/register/"
params = {"username": "example_user", "password": "example_password"}

response = requests.post(url, params=params)

print(response.status_code)
print(response.text)  # Print the response content

try:
    json_response = response.json()
    print(json_response)
except Exception as e:
    print(f"Error parsing JSON: {e}")
