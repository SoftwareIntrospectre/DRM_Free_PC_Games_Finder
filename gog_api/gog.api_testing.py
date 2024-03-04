import requests
import json

# gog_host = "https://api.gog.com/products/1207658691"
# # gog_host = "https://api.gog.com/products"

# r = requests.get(gog_host)

# # Check if the request was successful
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


gog_host = "https://api.gog.com/products"

r = requests.get(gog_host)

if r.status_code == 200:
    json_response = r.json()

else:
    print("Error:", r.status_code)
