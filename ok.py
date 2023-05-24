import requests

def login(username, password):
    url = 'https://b-api.facebook.com/method/auth.login'
    payload = {
        'username': username,
        'password': password
    }
    
    response = requests.post(url, data=payload)
    return response.json()
