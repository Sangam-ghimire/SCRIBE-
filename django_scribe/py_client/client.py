import requests

endpoint = "http://localhost:8000/book"

response= requests.get(endpoint) 
print(response.json())