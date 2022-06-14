import requests
import json

# GET GUILDS
def get_servers(token):
    url = 'https://discord.com/api/v9/users/@me/guilds'
    header = {"authorization": token}

    r = requests.get(url, headers=header)
    return r.json()

def get_members(token, server_id):
    url = 'https://discord.com/api/v9/guilds/{}/preview'.format(server_id)
    header = {"authorization": token}

    r = requests.get(url, headers=header)
    return r.json()["approximate_member_count"]

def get_online_members(token, server_id):
    url = 'https://discord.com/api/v9/guilds/{}/preview'.format(server_id)
    header = {"authorization": token}

    r = requests.get(url, headers=header)
    return r.json()["approximate_presence_count"]