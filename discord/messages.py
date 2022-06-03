import requests
import json
import time

token = 'OTY0OTE5NjQwMzE4OTM5MjY2.GMhLkk.OXSynpoVLuJYKCOc8NHaFfpbIoV-Dd8j0-IsPM'
channel_id = '982013142206931014'

message = "";
previous_message_id = ""

# POST MESSAGES
def send_message(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
    
    r = requests.post(url, data=data, headers=header)

# GET MESSAGES
def get_messages(token, channel_id, limit):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"limit": limit}
    header = {"authorization": token}

    r = requests.get(url, params=data, headers=header)
    return r.json()