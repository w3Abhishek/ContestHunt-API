import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# AtCoder API URL
ATCODER_API_URL = 'https://atcoder.jp/contests/'

# AtCoder API Headers
headers = {
  "user-agent": "Mozilla/5.0"
}

def fetch_contests():
    response = requests.get(ATCODER_API_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    contests_table = soup.find_all("tbody")[1].find_all("tr")
    contests = []
    for contest in contests_table:
        contest_info = {}
        contest_meta = contest.find_all("td")
        start_time_str = contest_meta[0].find("a")['href'].split('?iso=')[1].split('&')[0]
        duration_str = contest_meta[2].text
        start_time = datetime.strptime(start_time_str, "%Y%m%dT%H%M")
        start_time_epoch = int(start_time.timestamp())
        duration_parts = duration_str.split(":")
        duration = timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]))
        end_time_epoch = int((start_time + duration).timestamp())
        contest_info['name'] = contest_meta[1].find("a").text
        contest_info['start_time'] = start_time_epoch
        contest_info['end_time'] = end_time_epoch
        contest_info['duration'] = int(duration.total_seconds())
        contest_info['url'] = f'https://atcoder.jp{contest_meta[1].find("a")["href"]}'
        contest_info['description'] = ''
        contest_info['platform'] = 'atcoder'
        contests.append(contest_info)
    return contests