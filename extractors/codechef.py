import requests
from datetime import datetime

# Codechef API URL
CODECHEF_API_URL = 'https://www.codechef.com/api/list/contests/all'

# Codechef API Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

def fetch_contests():
    params = {
        'sort_by': 'START',
        'sorting_order': 'asc',
        'offset': 0,
        'mode': 'all'
    }
    response = requests.get(CODECHEF_API_URL, headers=headers).json()
    contests = []
    for contest in response['future_contests']:
        contest_info = {}
        contest_info['name'] = contest['contest_name']
        contest_info['url'] = f'https://www.codechef.com/{contest["contest_code"]}'
        contest_info['start_time'] = int(datetime.fromisoformat(contest['contest_start_date_iso']).timestamp())
        contest_info['end_time'] = int(datetime.fromisoformat(contest['contest_end_date_iso']).timestamp())
        contest_info['duration'] = int(contest_info['end_time'] - contest_info['start_time'])
        contest_info['description'] = ''
        contest_info['platform'] = 'codechef'
        contests.append(contest_info)
    return contests
