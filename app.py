import requests

response = requests.get("https://api.edamam.com/api/nutrition-data")
print(response.status_code)