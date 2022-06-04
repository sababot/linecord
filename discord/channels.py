import requests
import json

# GET GUILDS
def get_channels(token, server_id):
    url = 'https://discord.com/api/v9/guilds/{}/channels'.format(server_id)
    header = {"authorization": token}

    r = requests.get(url, headers=header)
    return r.json()