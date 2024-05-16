import requests
import os
import boto3
import json
import airflow


dag = airflow.DAG()

def gog_api_data_to_s3():

    response = requests.get('https://catalog.gog.com/v1/catalog')
    response_json = response.json()

    products = response_json['products']

    game_dictionaries_list = []

    for product in products:
        game_dictionary = {
            "game_id": None,
            "game_name": None,
            "developer_names": [],
            "publisher_names": [],
            "release_date": None,
            "operating_systems": []
            }

        game_dictionary["game_id"] = product['id']
        game_dictionary["game_name"] = product['title']
        game_dictionary["developer_names"] = product['developers']
        game_dictionary["publisher_names"] = product['publishers']
        game_dictionary["release_date"] = product['releaseDate']
        game_dictionary["operating_systems"] = product['operatingSystems']

        game_dictionaries_list.append(game_dictionary)

    for game in game_dictionaries_list:
        print(game)

    game_data_string = json.dumps(game_dictionaries_list, indent=4)

    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

    if not AWS_ACCESS_KEY or not AWS_SECRET_ACCESS_KEY:
        raise ValueError("AWS credentials are not set in environment variables.")

    bucket_name = 'drm-free-data-engineering-bucket'
    file_name = 'gog_api_games_list.json'

    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    # initialize S3 client
    s3 = session.client('s3')

    # Upload the file to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=game_data_string
    )

    print(f"File uploaded to S3 bucket '{bucket_name}' as '{file_name}'")


# gog_api_data_to_s3()