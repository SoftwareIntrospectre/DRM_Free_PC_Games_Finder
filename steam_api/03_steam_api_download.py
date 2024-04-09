# """Download data from the Steam API into a CSV. Handle errors, etc."""

# # Steam API does not refresh more than once a day, so there's no point in getting data more frequently than that.

# # standard library imports
# import csv
# import datetime as dt
# import json
# import os
# import statistics
# import time

# # third party library imports
# import numpy as np
# import pandas as pd
# import requests

# def get_request(url, parameters=None):
#     try:
#         response = requests.get(url=url, params=parameters)

#     except SSLError as s:
#         print('SSL Error:', s)

#         # Retry up to 5 times (base case of recursion)
#         for i in range(5, 0, -1):
#             print('\rWaiting... ({})'.format((i), end=''))

#             # pause 1 second in between
#             time.sleep(1)

#         print('\rRetrying.' + ' '*10)

#         # recursively try again
#         return get_request(url, parameters)

#     if response.status_code == 200:

#         json_data = response.text
#         return json_data
    
#     else:
#         print('No response')
        
#         # wait 10 seconds to try again
#         time.sleep(10)
#         print('Retrying.')
#         return get_request(url, parameters)
    

# url = "https://steamspy.com/api.php" # updates every 24 hours, so no need to do this more than once a day
# # parameters = {"request":"all"}
# parameters = {"request":"all"}


# json_data = get_request(url, parameters=parameters)
# #steam_spy_all_df = pd.DataFrame.from_dict(json_data, orient='index')
# steam_spy_all_df = pd.DataFrame.from_dict(json.loads(json_data), orient='index')
# #print(steam_spy_all_df)

# # generate sorted games_list from steamspy data

# games_list = steam_spy_all_df[:].sort_values('score_rank', ascending=False).reset_index(drop=True)
# print(games_list)

# #games_list = pd.read_csv('C:/Users/tchac/Downloads/steam_games_list_tc_custom.csv')

# def get_game_data(start, stop, parser, pause):
#     """Return list of app data generated from parser
    
#     parser : function to handle request"""

#     game_data = []

#     for index, row in games_list[start:stop].iterrows():
#         print('Current index: {}'.format(index), end='\r')
#         game_data_row = {}

#         for column_name, value in row.items():
#             game_data_row[column_name] = value

#         game_data.append(game_data_row)

#         time.sleep(pause)

#     print("get_game_data.game_data : ", game_data)
#     return game_data


# def process_batches(parser, games_list, download_filepath, data_filename, index_filename,
#                     columns, begin=0, end=-1, batchsize=100, pause=1):
#     """Process app data in batches, writing directly to file
    
#     parser: custom function to format GET request
#     game_list : dataframe of games from steam (all columns)
#     download_filepath : path to store the data as a CSV file
#     index_filename : filename to store the highest index written
#     columns : column_names for file
    
    
#     Keyword arguments:
#         begin : starting index (get from index_filename, default is 0)
#         end : index to finish (defaults to end of game_list)
#         batchsize : number of games to write in each batch (default is 1,000)
#         pause : seconds to wait after each API request (default = 1)
#         returns : None
#     """

#     print('Starting at index {}:\n'.format(begin))

#     # by default: process all games in the games_list0f
#     if end == -1:
#         end = len(games_list) + 1

#     # generate numpy (np) array of batches begin and end points
#         # Used to grab the contents of each list from 0 to the size of the list (up to the batch size's count)
#             # Example: process the list size, up to 999 rows per batch (1,000 being the batchsize)
#     batches = np.arange(begin, end, batchsize)
#     batches = np.append(batches, end)


#     # RESUME HERE: Monday 4/8/2024

#     games_written = 0
#     batch_times = []

#     for i in range(len(batches) - 1):
#         start_time = time.time()

#         start = batches[i]
#         stop = batches[i+1]

#         game_data = get_game_data(start, stop, parser, pause)

#         print("\n\nprocess_batches.game data: ", game_data)
#         relative_filepath = os.path.join(download_filepath, data_filename)

#         # writing app data to file: append new data 
#         with open(relative_filepath, 'a', newline='', encoding='utf-8') as f:

#             # ignores extra unexpected fields as they arise
#             writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')

#             #-------------------------------------------------------------------------------
#             # loop exists just to show the countdown, and to not interrupt.
#             for j in range(30,0,-1):
#                 print("\rAbout to write data, don't stop the script ({})".format(j), end="")
#                 time.sleep(1)

#             writer.writerows(game_data)
#             print("\rExported lines {}={} to {}".format(start, stop-1, data_filename), end= ' ')
#             #-------------------------------------------------------------------------------

#         games_written += len(game_data)

#         index_path = os.path.join(download_filepath, index_filename)

#         #writing the last index to file
#         with open(index_path, 'w') as f:
#             index = stop
#             print(index, file=f)

#         # logging time taken
#         end_time = time.time()
#         time_taken = end_time - start_time

#         batch_times.append(time_taken)
#         mean_time = statistics.mean(batch_times)

#         est_remaining = (len(batches) - i - 2) * mean_time

#         remaining_td = dt.timedelta(seconds=round(est_remaining))
#         time_td  = dt.timedelta(seconds=round(time_taken))
#         mean_td = dt.timedelta(seconds=round(mean_time))

#         print('Batch {} time: {} (avg: {}. remaining: {})'.format(i, time_td, mean_td, remaining_td))  

#     print('\nProcessing batches complete. {} apps written'.format(games_written))              


# def reset_index(download_path, index_filename):
#     """Reset index in file to 0.
#     This exists because data is loaded in batches, and this is necessary per batch.
#     Can be used to reset the data processing pipeline, and allows for more consistency and control"""

#     relative_filepath = os.path.join(download_path, index_filename)

#     with open(relative_filepath, 'w') as file:
#         print(0, file=file)


# def get_index(download_path, index_filename):
#     """Retrieve index from file, returning 0 if file not found"""
#     try:
#         relative_filepath = os.path.join(download_path, index_filename)

#         with open(relative_filepath, 'r') as file:
#             index = int(file.readline())

#     except FileNotFoundError:
#         index = 0

#     return index


# def prepare_data_file(download_path, filename, index, columns):
#     """Create file and write headers if index is 0"""
#     if index == 0:
#         relative_file_path = os.path.join(download_path, filename)

#         with open(relative_file_path, 'w', newline='') as file:
#             file_writer = csv.DictWriter(file, fieldnames=columns)
#             file_writer.writeheader()


# def parse_steam_request(game_id, name):
#     """Unique parser to handle data from Steam Store API

#     Returns  : json formatted (dict-like)
#     """

#     url = "https://store.steampowered.com/api/appdetails"
#     parameters = {"appids": game_id}

#     json_data = get_request(url, parameters=parameters)
#     json_game_data = json_data[str(game_id)]

#     if json_game_data['success']:
#         data = json_game_data['data']

#     else:
#         data = {'name': name, 'steam_appid': game_id}

#     return data

# def parse_steamspy_request(game_id, name):
#     """Parser to handle SteamSpy API data."""

#     url = "https://steamspy.com/api.php"
#     parameters = {"request": "appdetails", "appid":game_id}

#     json_data = get_request(url, parameters)
#     return json_data



# # driver code
# download_path = 'C:/Users/tchac/Downloads/'
# steamspy_game_data = 'steamspy_data_TC_custom_3.csv'
# steamspy_index = 'steamspy_index.txt'

# steamspy_columns = [
#     'appid', 'name', 'developer', 'publisher', 'score_rank', 'positive',
#     'negative', 'underscore', 'owners', 'average_forever', 'average_2weeks',
#     'median_forever', 'median_2weeks', 'price', 'initialprice', 'discount',
#     'languages', 'genre', 'ccu', 'tags'
# ]

# # resets index to 0 per download
# reset_index(download_path, steamspy_index)

# #grabs the current index
# index = get_index(download_path, steamspy_index)

# #only prepares file if index is set to 0 (hence why reset_index() is called)
# prepare_data_file(download_path, steamspy_game_data, index, steamspy_columns)

# process_batches(
#     parser=parse_steam_request,
#     games_list=games_list,
#     download_filepath=download_path,
#     data_filename=steamspy_game_data,
#     index_filename=steamspy_index,
#     columns=steamspy_columns,
#     begin=index,
#     end=10000,
#     batchsize=500,
#     pause=0.001
# )

# # inspect and download steamspy data
# pd.read_csv(f"{download_path}/{steamspy_game_data}").head()


# # can only make 100,000 calls to the web API per day







import csv
import datetime as dt
import json
import os
import statistics
import time

import numpy as np
import pandas as pd
import requests

def get_request(url, parameters=None):
    try:
        response = requests.get(url=url, params=parameters)
        response.raise_for_status()  # Raise error for non-200 status codes

    except (requests.HTTPError, requests.ConnectionError) as e:
        print('Error:', e)
        return None

    return response.json()

def process_data(download_filepath, data_filename, columns, batch_size=1000, pause=1):
    total_requests = 0
    total_entries = 0
    page = 0
    
    while total_entries < 100000:
        start_time = time.time()

        parameters = {"request": "all", "page": page}
        json_data = get_request("https://steamspy.com/api.php", parameters=parameters)

        if json_data is None:
            print('Failed to fetch data for page', page)
            time.sleep(pause)  # Wait before retrying
            continue

        games_list = pd.DataFrame.from_dict(json_data, orient='index')
        total_entries += len(games_list)

        relative_filepath = os.path.join(download_filepath, data_filename)
        mode = 'a' if total_requests > 0 else 'w'  # Append if not first batch

        with open(relative_filepath, mode, newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')

            for j in range(3, 0, -1):
                print("\rWriting data (Page {}, Attempt {}), don't stop the script...".format(page, j), end='')
                time.sleep(0.5)

            games_list.to_csv(f, header=f.tell()==0, index=False)

        total_requests += 1
        page += 1

        # Throttle requests to stay within the limit
        elapsed_time = time.time() - start_time
        remaining_time = max(0, 60 - elapsed_time)
        time.sleep(remaining_time)

    print('\nProcessing complete. Total entries written:', total_entries)

download_path = 'C:/Users/tchac/Downloads/'
steamspy_game_data = 'steamspy_data_TC_custom_4.csv'
steamspy_columns = [
    'appid', 'name', 'developer', 'publisher', 'score_rank', 'positive',
    'negative', 'underscore', 'owners', 'average_forever', 'average_2weeks',
    'median_forever', 'median_2weeks', 'price', 'initialprice', 'discount',
    'languages', 'genre', 'ccu', 'tags'
]

process_data(download_path, steamspy_game_data, steamspy_columns)
