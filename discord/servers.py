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

servers = get_servers("MzU4MzM3OTgxMjk3NDU5MjAx.G7gIdP.cr1o3Tas5z7Z6C_SzC9il9p46GWfPU0s8Tpshw")
print(servers)