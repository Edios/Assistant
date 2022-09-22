import requests


def send_post_request(url, data)->dict:
    response = requests.post(url,data)
    return response.json()