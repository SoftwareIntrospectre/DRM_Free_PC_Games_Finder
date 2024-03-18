'''
    pip3 install steam
    pip3 install gevent
    pip3 install eventemitter
    pip3 install requests
    pip3 install google
'''

import os
from steam.client import SteamClient

# Check if 'STEAM_API_KEY' is available in environment variables
steam_api_key = os.environ.get('STEAM_API_KEY')

def api_key_is_valid(steam_api_key):
    if not steam_api_key:
        raise ValueError("No Steam API Key Found")
    else:
        print("Steam API Key found.")
        return True

# Initialize Steam client
client = SteamClient()

# Check if the provided Steam API key is valid
if api_key_is_valid(steam_api_key):
    client.api_key = steam_api_key

    # Replace app_id with the desired game's AppID
    game_info = client.app(app_id=570)  # Example: Dota 2 (AppID: 570)

    print(game_info)
