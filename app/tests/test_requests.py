import requests

BASE_URL = "http://localhost:8000/get_form"

def test_valid_form():
    data = {
        "name": "Vasya",
        "email": "test@example.com",
        "phone": "+71234567890"

    }
    response = requests.post(BASE_URL, data=data)
    print("Response:", response.json())

def test_invalid_form():
    data = {
        "email": "test@example.com",
        "unknown_field": "some_value"
    }
    response = requests.post(BASE_URL, data=data)
    print("Response:", response.json())

if __name__ == "__main__":
    test_valid_form()
    test_invalid_form()
