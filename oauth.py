from __future__ import absolute_import, print_function 

import tweepy

consumer_key="qq7fYUftibejNxw2rHuiC9FmC"
consumer_secret="hLuMT3N8oVNgH5CPKKuTlaB85IiQ0Ga1VFHf1sg0zqEAIaB0tY"

access_token="68931432-6lPNWYesN7Co7Qb8q5uekUusLI4F54ZZesDmI7X5l"
access_token_secret="d2Eq0tKjyobmAFNiv1CKATvkZIWz2G2xrhv1CoGaQk9nH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(api.me().name)

public_tweets = api.home_timeline()
count = 0
for tweet in public_tweets:
    print(tweet.text)
    count += 1
print(count)
print("===================")

user = api.me()
print(user.screen_name)
print(user.followers_count)
count = 0
for friend in user.friends():
    print(friend.screen_name)
    count += 1
print(count)
print("===================")

#api.update_status(status='Updating using OAuth authentication via Tweepy!')
