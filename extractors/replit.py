import requests, json
from datetime import datetime



# Repl.it API URL
REPLIT_API_URL = 'https://replit.com/graphql'

# Repl.it API Headers
REPLIT_API_HEADERS = {
    'referer': 'https://replit.com/bounties?status=open&order=creationDateDescending',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-client-version': 'fec03889',
    'x-forwarded-host': 'replit.com',
    'x-kitchen': 'false',
    'x-requested-with': 'XMLHttpRequest',
}

def fetch_bounties():
    bounties = []
    tick = 0
    while True:
        json_data = [{
                "query": "query BountiesPageSearch($input: BountySearchInput!) { bountySearch(input: $input) { __typename ... on BountySearchConnection { items { ...BountyCard __typename } pageInfo { hasNextPage nextCursor __typename } __typename } ... on UserError { message __typename } ... on UnauthorizedError { message __typename } } } fragment BountyCard on Bounty { id title descriptionPreview cycles deadline status slug solverPayout timeCreated applicationCount isUnlisted solver { id username image url __typename } user { id username image url __typename } __typename }",
                "variables": {
                    "input": {
                        "after": str(tick),
                        "count": 10,
                        "searchQuery": "",
                        "statuses": ["open"],
                        "order": "creationDateDescending",
                        "listingState": "listed"
                    }
                }
            }]
        response = requests.post(REPLIT_API_URL, headers=REPLIT_API_HEADERS, json=json_data).json()
        data = response[0]
        for bounty in data['data']['bountySearch']['items']:
            start_time = datetime.fromisoformat(bounty['timeCreated'].replace('Z', '+00:00'))
            end_time = datetime.fromisoformat(bounty['deadline'].replace('Z', '+00:00'))
            bounties.append({
                'name': bounty['title'],
                'description': bounty['descriptionPreview'],
                'start_time': int(start_time.timestamp()),
                'end_time': int(end_time.timestamp()),
                'duration': int((end_time - start_time).total_seconds()),
                'url': f'https://replit.com/bounties/{bounty["slug"]}',
                'amount': float(bounty['cycles'] / 100)
            })
        if not data['data']['bountySearch']['pageInfo']['hasNextPage']:
            break
        print(data['data']['bountySearch']['pageInfo']['nextCursor'])
        tick += 10
    return bounties

with open('bounties.json', 'w') as f:
    json.dump(fetch_bounties(), f, indent=4)



# def fetch_bounties():
#     hasmore = True
#     bounties = []
#     tick = 0
#     while hasmore:
#         json_data = [
#             {
#   "query": "query BountiesPageSearch($input: BountySearchInput!) { bountySearch(input: $input) { __typename ... on BountySearchConnection { items { ...BountyCard __typename } pageInfo { hasNextPage nextCursor __typename } __typename } ... on UserError { message __typename } ... on UnauthorizedError { message __typename } } } fragment BountyCard on Bounty { id title descriptionPreview cycles deadline status slug solverPayout timeCreated applicationCount isUnlisted solver { id username image url __typename } user { id username image url __typename } __typename }",
#   "variables": {
#     "input": {
#       "after": None,
#       "count": 10,
#       "searchQuery": "",
#       "statuses": ["open"],
#       "order": "creationDateDescending",
#       "listingState": "listed"
#     }
#   }
# }

#         ]

#         response = requests.post('https://replit.com/graphql', headers=headers, json=json_data)
#         data = response.json()[0]
#         for bounty in data['data']['bountySearch']['items']:
#             start_time = datetime.fromisoformat(bounty['timeCreated'].replace('Z', '+00:00'))
#             end_time = datetime.fromisoformat(bounty['deadline'].replace('Z', '+00:00'))
            
#             bounties.append({
#                 'name': bounty['title'],
#                 'description': bounty['descriptionPreview'],
#                 'start_time': int(start_time.timestamp()),  # Convert to epoch time
#                 'end_time': int(end_time.timestamp()),  # Convert to epoch time
#                 'duration': int((end_time - start_time).total_seconds()),  # Calculate duration in seconds
#                 'url': f'https://replit.com/bounties/{bounty["slug"]}',
#                 'amount': float(bounty['cycles'] / 100)
#             })
#         json_data[0]['variables']['input']['after'] = str(tick)
#         hasmore = data['data']['bountySearch']['pageInfo']['hasNextPage']
#         if hasmore:
#             tick += 10
#         print(data['data']['bountySearch']['items'][0]['title'])
#         print(f"Tick: {tick} - Hasmore: {hasmore} - Bounties: {len(bounties)} - Response: {response.status_code}")
        
#     return bounties

# with open('bounties.json', 'w') as f:
#     json.dump(fetch_bounties(), f, indent=4)