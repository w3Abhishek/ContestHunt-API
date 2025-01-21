import requests
from datetime import datetime

# TopCoder API URL
TOPCODER_API_URL = 'https://api.topcoder.com/v5/challenges/?status=Active'

# TopCoder API Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

def fetch_contests():
    response = requests.get(TOPCODER_API_URL, headers=headers).json()
    contests = []
    
    for contest in response:
        contest_info = {}
        contest_info['name'] = contest['name']
        contest_info['url'] = f'https://www.topcoder.com/challenges/{contest["id"]}'
        contest_info['start_time'] = int(datetime.fromisoformat(contest['startDate'].replace('Z', '+00:00')).timestamp())
        contest_info['end_time'] = int(datetime.fromisoformat(contest['endDate'].replace('Z', '+00:00')).timestamp())
        contest_info['duration'] = contest_info['end_time'] - contest_info['start_time']
        contest_info['description'] = contest['description']
        contest_info['platform'] = 'topcoder'
        contests.append(contest_info)
    return contests