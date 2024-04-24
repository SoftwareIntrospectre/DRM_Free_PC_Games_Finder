import os
import pandas as pd

directory_to_check = 'C:/Users/tchac/Documents/Projects/DRM_Free_VideoGames_DE_Pipeline_Project'
file_to_check = 'GOG_GameNames_and_GameIDs.txt'

fully_qualified_file = os.path.join(directory_to_check, file_to_check)

print(fully_qualified_file)

file_df = pd.read_csv(fully_qualified_file, quotechar='^', sep='|')

print(file_df)