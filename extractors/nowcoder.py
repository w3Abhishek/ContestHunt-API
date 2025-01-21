import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

# NowCoder API URL
NOWCODER_API_URL = 'https://ac.nowcoder.com/acm/contest/vip-index'

# NowCoder API Headers
headers = {
  "user-agent": "Mozilla/5.0"
}

def fetch_contests():
    response = requests.get(NOWCODER_API_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    upcoming_contests_section = soup.find("div", class_="js-current")
    contests_data = upcoming_contests_section.find_all("div", class_="platform-item")
    contests = []
    for contest in contests_data:
        contest_info = {}
        contests_json_data = json.loads(contest['data-json'].replace("&quot;", '"').replace("&amp;", "&"))
        contest_info['ame'] = contests_json_data['contestName']
        contest_info['start_time'] = contests_json_data['contestStartTime']
        contest_info['duration'] = contests_json_data['contestDuration']
        contest_info['end_time'] = contests_json_data['contestEndTime']
        contest_info['url'] = f'https://ac.nowcoder.com/acm/contest/{contests_json_data["contestId"]}'
        contest_info['description'] = ''
        contest_info['platform'] = 'nowcoder'
    return contests

print(fetch_contests())