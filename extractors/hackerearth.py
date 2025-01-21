import requests
from datetime import datetime

# HackerEarth API URL
HACKEREARTH_API_URL = 'https://www.hackerearth.com/chrome-extension/events/'

# HackerEarth API Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

def fetch_contests():
    response = requests.get(HACKEREARTH_API_URL, headers=headers).json()
    contests = []
    for contest in response['response']:
        contest_info = {}
        contest_info['name'] = contest['title']
        contest_info['url'] = contest['url']
        contest_info['start_time'] = int(datetime.fromisoformat(contest['start_utc_tz']).timestamp())
        contest_info['end_time'] = int(datetime.fromisoformat(contest['end_utc_tz']).timestamp())
        contest_info['duration'] = int(contest_info['end_time'] - contest_info['start_time'])
        contest_info['description'] = contest['description']
        contest_info['platform'] = 'hackerearth'
        contests.append(contest_info)
    return contests