import requests
import json

# GET USERNAME
def get_username(token):
    url = 'https://discord.com/api/v9/users/@me'
    header = {"authorization": token}

    r = requests.get(url, headers=header)
    return r.json()

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