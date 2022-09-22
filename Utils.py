import json
import os
from pathlib import Path
import requests
from requests import auth

USER_DATA_FOLDER=Path('UserData')
BIKE_SERVICE_INFO_FILENAME='bike_service_information.json'

class BearerToken(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def send_post_request(url, data)->dict:
    response = requests.post(url,data)
    return response.json()

def send_get_request(url,bearer_token)->dict:
    response = requests.get(url,auth=BearerToken(bearer_token))
    return response.json()

#serialize
def save_user_data_to_json(filename, data):
    """
    All acuired user data is stored in [ProjectRoot]/UserData folder.
    :param filename: Name of json file
    :param data: Dict data to write
    :return: None
    """
    if not USER_DATA_FOLDER.is_dir():
        os.mkdir(USER_DATA_FOLDER)
    with open(USER_DATA_FOLDER / filename, 'w') as file:
        json.dump(data,file)
#deserialize
def read_user_data_from_json(filename):
    """
    Read JSON file stored in [ProjectRoot]/UserData folder.
    :param filename:
    :return:
    """
    file_path=USER_DATA_FOLDER / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Could not find file: {file_path}")
    with open(file_path,'r') as file:
        lines=file.readlines()
        return json.loads(lines[0])
