import requests
from bs4 import BeautifulSoup

url = "https://gogapidocs.readthedocs.io/en/latest/gameslist.html"

response = requests.get(url)

# using lxml because recommended by documentation as faster (upside: faster, downside: has external C dependency)
soup = BeautifulSoup(response.content, "lxml")

# used to see the HTML structure of the web page
print(soup.prettify())

# found the table containing the relevant data
game_data_table = soup.find("table", class_="docutils")

print(game_data_table)

games_names_and_ids_dict_list = []

# looking for all rows except for the first one
for row in game_data_table.find_all("tr")[1:]:
    columns = row.find_all("td")

    # game name is the first column in the table and remove all tags
    game_name = columns[0].get_text(strip=True)

    # game id is the second column in the table and remove all tags
    game_id = columns[1].get_text(strip=True)

    # print(game_name)
    # print(game_id)

    # add a dictionary that maps the game name to the first column's value, and the game id to the second column's value for every row.
    games_names_and_ids_dict_list.append({"GameName": game_name, "GameId": game_id})

print(games_names_and_ids_dict_list)