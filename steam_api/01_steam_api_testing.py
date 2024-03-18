import os

steam_api_key = os.environ.get('STEAM_API_KEY')
steam_domain_name = os.environ.get('STEAM_DOMAIN_NAME')

if not steam_api_key:
    raise ValueError("No Steam API Key Found")

else:
    print("Steam API Key found.")

if not steam_domain_name:
    raise ValueError("No Steam Domain Name Found")

else:
    print("Steam Domain Name found.")