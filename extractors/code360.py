import requests
import datetime
# Code360 CodingNinja Naukri.com API URL
CODE360_API_URL = "https://www.naukri.com/code360/api/v4/public_section/contest_list"

# Code360 CodingNinja Naukri.com API Headers
headers = {"user-agent": "Mozilla/5.0", "accept": "application/json"}

def fetch_contests():
    response = requests.get(CODE360_API_URL, headers=headers).json()
    contests = []
    for contest in response['data']['events']:
        if contest['registration_end_time'] < datetime.datetime.now().timestamp():
            continue
        contest_info = {}
        contest_info['name'] = contest['name']
        contest_info['start_time'] = contest['registration_start_time']
        contest_info['end_time'] = contest['event_end_time']
        contest_info['duration'] = contest['event_start_time'] - contest['event_end_time']
        contest_info['url'] = f'https://www.naukri.com/code360/contests/{contest["slug"]}'
        contest_info['description'] = contest['short_desc']
        contests.append(contest)
    return contests