import requests
from datetime import datetime

# Codeforces API URL
CODEFORCES_API_URL = 'https://codeforces.com/api/contest.list'

# Codeforces API Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

def fetch_contests():
    response = requests.get(CODEFORCES_API_URL, headers=headers).json()
    contests = []
    current_epoch_time = int(datetime.now().timestamp())  # Convert current time to epoch

    for contest in response['result']:
        contest_info = {}
        if contest['phase'] != 'BEFORE' or contest['startTimeSeconds'] < current_epoch_time:
            continue
        contest_info['name'] = contest['name']
        contest_info['url'] = f'https://codeforces.com/contestRegistration/{contest["id"]}'
        contest_info['start_time'] = contest['startTimeSeconds']
        contest_info['end_time'] = contest['startTimeSeconds'] + contest['durationSeconds']
        contest_info['duration'] = contest['durationSeconds']
        contest_info['description'] = ''
        contest_info['platform'] = 'codeforces'
        contests.append(contest_info)
    return contests

print(fetch_contests())