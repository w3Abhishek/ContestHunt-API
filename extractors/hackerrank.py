import requests
from datetime import datetime

# HackerRank API URL
HACKERRANK_API_URL = 'https://www.hackerrank.com/community/engage/events'

# HackerRank API Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

def fetch_contests():
    response = requests.get(HACKERRANK_API_URL, headers=headers).json()
    contests = []
    for contest in response['data']['events']['ongoing_events']:
        contest_info = {}
        contest = contest['attributes']
        contest_info['name'] = contest['name']
        contest_info['url'] = contest['microsite_url']
        contest_info['start_time'] = int(datetime.fromisoformat(contest['start_time'].replace('Z', '+00:00')).timestamp())
        contest_info['end_time'] = int(datetime.fromisoformat(contest['end_time'].replace('Z', '+00:00')).timestamp())
        contest_info['duration'] = int(contest_info['end_time'] - contest_info['start_time'])
        contest_info['description'] = contest['description']
        contest_info['platform'] = 'hackerrank'
        contests.append(contest_info)
    return contests