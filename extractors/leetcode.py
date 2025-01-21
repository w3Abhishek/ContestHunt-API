import requests, time, json

# Leetcode API URL
LEETCODE_API_URL = 'https://leetcode.com/graphql'

# Leetcode API Headers
LEETCODE_API_HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}

def fetch_contests():
    query = '''
    {
        allContests {
                    title
                    titleSlug
                    startTime
                    duration
                    description
        }
    }
    '''
    payload = {
        'operationName': None,
        'variables': {},
        'query': query,
    }
    response = requests.post(LEETCODE_API_URL, headers=LEETCODE_API_HEADERS, json=payload).json()
    all_contests = response['data']['allContests']
    contests = []
    for contest in all_contests:
        contest_info = {}
        # Skip past contests
        if contest['startTime'] + contest['duration'] < time.time():
            continue
        contest_info['name'] = contest['title']
        contest_info['url'] = f'https://leetcode.com/contest/{contest["titleSlug"]}'
        contest_info['start_time'] = contest['startTime']
        contest_info['end_time'] = contest['startTime'] + contest['duration']
        contest_info['duration'] = contest['duration']
        contest_info['description'] = contest['description']
        contests.append(contest_info)
    return contests