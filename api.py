import os
import json

from time import sleep
from hashlib import md5

import requests

base_url = 'https://webapi.asianodds88.com/AsianOddsService'
username = os.getenv('API_USERNAME')
password = md5(os.getenv('API_PASSWORD').encode('utf-8')).hexdigest()


def login():
    url = base_url + f'/Login?username={username}&password={password}'
    # print(url)
    r = requests.get(url, headers={'Accept': 'application/json'})
    content = json.loads(r.content)
    # print(content)
    token = content['Result']['Token']
    key = content['Result']['Key']
    new_url = content['Result']['Url']
    return token, key, new_url


def register(token, key, new_url):
    url = new_url + f'/Register?username={username}'
    requests.get(url, headers={
        'Accept': 'application/json',
        'AOKey': key,
        'AOToken': token
    }, timeout=10)


def request(url, token):
    # print(url)
    r = requests.get(url, headers={'AOToken': token})
    # print(r.content)
    try:
        content = json.loads(r.content)
        print(content)
    except:
        print(r.content)


sport = 1  # Football
market = 2  # 0 = Live, 1 = Today, 2 = Early
league = "-1612561053"  # *ENGLISH PREMIER LEAGUE - TO KICK OFF
oddsformat = "00"  # Europe


def get_sports(url, token):
    url = url + '/GetSports'
    request(url, token)


def get_leagues(url, token):
    url = f"{url}/GetLeagues?sportsType={sport}&marketTypeId={market}&bookies=ALL"
    request(url, token)


def get_matches(url, token):
    url = f"{url}/GetMatches?sportsType={sport}&marketTypeId={market}&bookies=ALL&leagues={league}"
    request(url, token)


def get_feeds(url, token):
    url = f"{url}/GetFeeds?sportsType={sport}&marketTypeId={market}&bookies=ALL&leagues={league}&oddsFormat={oddsformat}"
    request(url, token)


token, key, new_url = login()
sleep(3)
register(token, key, new_url)

# get_sports(new_url, token)
# get_leagues(new_url, token)
# get_matches(new_url, token)
get_feeds(new_url, token)
