import requests

# Your API key
api_key = 'YOUR_API_KEY'

# URL of the endpoint to retrieve the list of games
url = 'https://api.gog.com/products'

# Parameters including your API key for authentication
params = {'apiKey': api_key}

# Make a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    games_data = response.json()

    # Extract the list of game IDs
    game_ids = [game['id'] for game in games_data['products']]
    
    # Print the list of game IDs
    print(game_ids)
else:
    print(f"Failed to fetch data: {response.status_code} - {response.reason}")



#-----------------------------------------------------------------------------

# import requests
# import json

# gog_host = "https://api.gog.com/products/1207658948"
# # gog_host = "https://api.gog.com/products"

# r = requests.get(gog_host)

# # # Check if the request was successful
# if r.status_code == 200:
#     json_response = r.json()

#     # Extracting the relevant properties I want
#     game_id = json_response["id"]
#     title = json_response["title"]
#     content_system_compatability = json_response["content_system_compatibility"]

#     # nested property
#     product_card = json_response["links"]["product_card"]

#     game_data = {
#               "id": game_id,
#         "title": title,
#         "content_system_compatability": content_system_compatability,
#         "product_card": product_card
#     }

#     print(game_data)
    
# else:
#     print("Error:", r.status_code)

#--------------------------------------------------


# gog_host = "https://api.gog.com/products"

# r = requests.get(gog_host)

# if r.status_code == 200:
#     json_response = r.json()

# else:
#     print("Error:", r.status_code)
