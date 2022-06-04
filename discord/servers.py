import requests
import json

# GET GUILDS
def get_servers(token):
    url = 'https://discord.com/api/v9/users/@me/guilds'
    header = {"authorization": token}

    r = requests.get(url, headers=header)
    return r.json()