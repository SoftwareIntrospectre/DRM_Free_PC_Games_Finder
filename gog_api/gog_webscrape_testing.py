# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# url = "https://gogapidocs.readthedocs.io/en/latest/gameslist.html?highlight=id"

# # Send a GET request to the webpage
# response = requests.get(url)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all elements with the class "highlight-python"
# games_elements = soup.find_all("div", class_="highlight-python")

# # Initialize an empty list to store the dictionaries
# games_list = []

# # Loop through each game element
# for game_element in games_elements:
#     # Extract the Game Name and ID from the element text
#     game_name = game_element.find("span", class_="s2").text.strip()
#     game_id = game_element.find("span", class_="mi").text.strip()
    
#     # Create a dictionary for the current game and append it to the list
#     games_list.append({"GameName": game_name, "ID": game_id})

# # Print the list of dictionaries
# print(games_list)
