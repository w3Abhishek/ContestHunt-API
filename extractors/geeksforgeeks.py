import requests
from datetime import datetime

# GeeksforGeeks API URL
GEEKSFORGEEKS_API_URL = 'https://practiceapi.geeksforgeeks.org/api/vr/events/'

# GeeksforGeeks API Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

def fetch_contests():
    params = {
        'page_number': 1,
        'sub_type': 'all',
        'type': 'contest'
    }
    response = requests.get(GEEKSFORGEEKS_API_URL, headers=headers, params=params).json()
    contests = []
    for contest in response['results']['upcoming']:
        contest_info = {}
        contest_info['name'] = contest['name']
        contest_info['url'] = f'https://practice.geeksforgeeks.org/contest/{contest['slug']}'
        contest_info['start_time'] = int(datetime.strptime(contest['start_time'], "%Y-%m-%dT%H:%M:%S").timestamp())
        contest_info['end_time'] = int(datetime.strptime(contest['end_time'], "%Y-%m-%dT%H:%M:%S").timestamp())
        contest_info['duration'] = int(contest_info['end_time'] - contest_info['start_time'])
        contest_info['description'] = ''
        contest_info['platform'] = 'geeksforgeeks'
        contests.append(contest_info)
    return contests