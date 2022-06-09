import tweepy
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

api_key =  os.getenv('api_key')
api_secrets = os.getenv('api_secrets')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

selectedWord = None

if len(sys.argv) > 1:
    selectedWord = sys.argv[1]
else:
    sys.exit('Need a word to lookup')

# auth
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

screen_name = "evenstensberg"
friends = []

# iter pages
for page in tweepy.Cursor(api.get_followers, screen_name=screen_name,
                          count=200).pages(10):
    for user in page['users']:
        if selectedWord in user['description']:
            metadata = f"{user['id']} - {user['name']} (@{user['screen_name']})"
            friends.append(metadata)
    

print(json.dumps(friends, sort_keys=False, indent=4))