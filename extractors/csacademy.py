import requests
from datetime import datetime

# CSAcademy API URL
CSACADEMY_API_URL = 'https://csacademy.com/contests/?'

# CSAcademy API Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
    "x-requested-with": "XMLHttpRequest"
}

def fetch_contests():
    response = requests.get(CSACADEMY_API_URL, headers=headers).json()
    contests = []
    current_epoch_time = int(datetime.now().timestamp())  # Convert current time to epoch

    for contest in response['state']['Contest']:
        contest_info = {}
        if contest['startTime'] is None or int(contest['startTime']) < current_epoch_time:
            continue
        contest_info['name'] = contest['longName']
        contest_info['url'] = f'https://csacademy.com/contest/{contest["name"]}'
        contest_info['start_time'] = int(contest['startTime'])
        contest_info['end_time'] = int(contest['endTime'])
        contest_info['duration'] = contest_info['end_time'] - contest_info['start_time']
        contest_info['description'] = ''
        contests.append(contest_info)
    return contests