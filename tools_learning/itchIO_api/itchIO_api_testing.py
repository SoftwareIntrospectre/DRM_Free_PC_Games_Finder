import requests

def fetch_game_metadata(query):
    # Define endpoint URL for searching games
    endpoint_url = "https://itch.io/api/1/search"

    # Define query parameters
    params = {
        "q": query,          # Search query
        "type": "game",      # Type of content (game)
        "page": 1,           # Page number (optional)
        "return_metadata": 1 # Include metadata fields in response
    }

    try:
        # Make a GET request to the itch.io API
        response = requests.get(endpoint_url, params=params)
        response.raise_for_status()  # Raise an error for non-200 status codes
        return response.json()      # Parse and return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None

# Example search query (e.g., "action games")
query = "action games"

# Fetch game metadata
games_data = fetch_game_metadata(query)

# Check if the fetch was successful
if games_data:
    # Extract relevant metadata from the response
    for game in games_data.get("search"):
        game_id = game.get("id")
        game_name = game.get("title")
        game_publisher = game.get("publisher")
        game_developer = game.get("developer")
        game_price = game.get("price")
        # You can extract more metadata as needed
        
        # Print or process the metadata
        print(f"ID: {game_id}")
        print(f"Name: {game_name}")
        print(f"Publisher: {game_publisher}")
        print(f"Developer: {game_developer}")
        print(f"Price: {game_price}")
        print("---")
else:
    print("Failed to fetch game metadata.")
