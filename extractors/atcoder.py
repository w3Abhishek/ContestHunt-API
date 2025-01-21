import requests
from datetime import datetime
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
        contest_info['name'] = contest_meta[1].find("a").text
        contest_info['start_time'] = contest_meta[0].find("a")['href'].split('?iso=')[1].split('&')[0]
        contest_info['duration'] = contest_meta[2].text
        contest_info['url'] = f'https://atcoder.jp{contest_meta[1].find("a")["href"]}'
        contest_info['description'] = ''
        contests.append(contest_info)
    return contests