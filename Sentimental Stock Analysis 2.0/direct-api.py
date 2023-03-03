import requests, pandas as pd

app_id = '_8nO5QsB95hHFxNstUTWcw'
secret = 'a6RN-49DdN9r4q5DlNvQn7nbaHHKrQ'
auth = requests.auth.HTTPBasicAuth(app_id, secret)
reddit_username = 'TheHornyKid17'
reddit_password = 'vibhor05'

data = {
'grant_type': 'password',
'username': reddit_username,
'password': reddit_password
}

headers = {'User-Agent': 'Tutorial2/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
auth=auth, data=data, headers=headers)

token = res.json()['access_token']
headers['Authorization'] = 'bearer {}'.format(token)
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

print(res)
# https://www.reddit.com/r/wallstreetbets/top/?t=month
# https://www.reddit.com/r/wallstreetbets/top/?t=month&f=flair_name%3A"Stocks"

api = 'https://oauth.reddit.com'
res = requests.get('{}/r/wallstreetbets/top/?t=month'.format(api), headers=headers, params={'limit': '100'})
# print(res.json())

df = pd.DataFrame({'name': [], 'title': [], 'selftext': [], 'score': []})
# for post in res.json()['data']['children']:
#   df = df.append({
#     'name': post['data']['name'],
#     'title': post['data']['title'],
#     'selftext': post['data']['selftext'],
#     'score': post['data']['score']}, ignore_index=True)
# print(df)


while True:
#   res =     requests.get('{}/r/wallstreetbets/top/?t=month'.format(api),headers=headers, params={'limit': '100','after': df['name'].iloc[len(df) - 1]})
  res = requests.get('{}/r/wallstreetbets/top/?t=month'.format(api), headers=headers, params={'limit': '100'})
  if len(res.json()['data']['children']) == 0:
    print('No more posts found')
    break
  for post in res.json()['data']['children']:
    df = df.append({
    'name': post['data']['name'], 
      'title': post['data']['title'],
      'selftext': post['data']['selftext'],
      'score': post['data']['score']}, ignore_index=True)
print(df.tail())