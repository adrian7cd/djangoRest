import requests

endpoint = "http://localhost:8000/api/products/" # API Endpoint

data = {
  "title": "Product 1",
  "price": 32.55
}

get_response = requests.post(endpoint, json=data) # HTTP Request

print(get_response.json())