import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API credentials
app_id = os.getenv('EDAMAM_APP_ID')
app_key = os.getenv('EDAMAM_APP_KEY')

food_input = input("Enter food: ")

def get_nutrition_info(food_item):
    # API Endpoint
    url = "https://api.edamam.com/api/nutrition-data"

    # Required Parameters
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "ingr": food_item
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Print the response
    if response.status_code == 200:
        data = response.json()  # Convert the response to a Python dictionary
        print(data)  # Show the retrieved information
    else:
        print(f"Error: {response.status_code}")
        
get_nutrition_info(food_input)