import imp
import requests

endpoint = "http://localhost:8000/api/" # API Endpoint

get_response = requests.post(endpoint, json={"title": "Hello World"}) # HTTP Request
print(get_response.json())