import os
import json

from hashlib import md5

import requests

base_url = 'https://webapi.asianodds88.com/AsianOddsService'
username = os.getenv('API_USERNAME')
password = md5(os.getenv('API_PASSWORD').encode('utf-8')).hexdigest()


def login():
    print("Login")
    url = base_url + f'/Login?username={username}&password={password}'
    print(url)
    r = requests.get(url, headers={'Accept': 'application/json'})
    content = json.loads(r.content)
    print(content)
    token = content['Result']['Token']
    key = content['Result']['Key']
    new_url = content['Result']['Url']
    return token, key, new_url


def register(token, key, new_url):
    print("Register")
    url = new_url + f'/Register?username={username}'
    print(url)
    r = requests.get(url, headers={
        'Accept': 'application/json',
        'AOKey': key,
        'AOToken': token
    }, timeout=5)
    content = json.loads(r.content)
    print(content)


token, key, new_url = login()
register(token, key, new_url)
