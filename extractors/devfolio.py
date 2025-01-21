import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

# Devfolio API URL
DEVFOLIO_API_URL = 'https://api.devfolio.co/api/search/hackathons'

# Devfolio API Headers
headers = {
  "user-agent": "Mozilla/5.0"
}

def fetch_contests():
    # Fetching ongoing hackathons
    json_data = {
        'type': 'application_open',
        'from': 0,
        'size': 100,
    }
    response = requests.post(DEVFOLIO_API_URL, headers=headers, json=json_data)
    contests = []
    for contest in response.json()['hits']['hits']:
        contest_info = {}
        contest = contest['_source']
        contest_info['name'] = contest['name']
        contest_info['url'] = f"https://{contest['slug']}.devfolio.co/"
        contest_info['start_time'] = int(datetime.fromisoformat(contest['starts_at']).timestamp())
        contest_info['end_time'] = int(datetime.fromisoformat(contest['ends_at']).timestamp())
        contest_info['duration'] = int(contest_info['end_time'] - contest_info['start_time'])
        contest_info['description'] = contest['desc']
        contest_info['platform'] = 'devfolio'
        if contest['is_online']:
            contest_info['mode'] = 'online'
        else:
            contest_info['mode'] = 'offline'
        contests.append(contest_info)
    # Fetching upcoming hackathons
    json_data['type'] = 'upcoming'
    response = requests.post(DEVFOLIO_API_URL, headers=headers, json=json_data)
    for contest in response.json()['hits']['hits']:
        contest_info = {}
        contest = contest['_source']
        contest_info['name'] = contest['name']
        contest_info['url'] = f"https://{contest['slug']}.devfolio.co/"
        contest_info['start_time'] = int(datetime.fromisoformat(contest['starts_at']).timestamp())
        contest_info['end_time'] = int(datetime.fromisoformat(contest['ends_at']).timestamp())
        contest_info['duration'] = int(contest_info['end_time'] - contest_info['start_time'])
        contest_info['description'] = contest['desc']
        contest_info['platform'] = 'devfolio'
        if contest['is_online']:
            contest_info['mode'] = 'online'
        else:
            contest_info['mode'] = 'offline'
        contests.append(contest_info)
    return contests

print(fetch_contests())