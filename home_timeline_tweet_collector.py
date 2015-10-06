from __future__ import absolute_import, print_function 
import tweepy
import psycopg2
import psycopg2.extras
import sys
import re


#define token 
consumer_key="qq7fYUftibejNxw2rHuiC9FmC"
consumer_secret="hLuMT3N8oVNgH5CPKKuTlaB85IiQ0Ga1VFHf1sg0zqEAIaB0tY"

access_token="68931432-6lPNWYesN7Co7Qb8q5uekUusLI4F54ZZesDmI7X5l"
access_token_secret="d2Eq0tKjyobmAFNiv1CKATvkZIWz2G2xrhv1CoGaQk9nH"

#set authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

#create API
api = tweepy.API(auth)

#create connection
try:
  conn = psycopg2.connect("dbname='ml_projects' user='yahyaeru' host='localhost' password='secret'")
  conn.autocommit = True
except:
  print("Cannot connect to database")

#create cursor
cursor = conn.cursor()

print(".................")
least_id = 0

try:
  cursor.execute("SELECT min(id) FROM home_status;")
  row = cursor.fetchall()
  least_id = row[0][0]
  print(least_id)
except Exception as e:
  print("Cannot get least_id")
  print(e)


public_tweets = api.home_timeline(max_id=651204327931940864,count = 100)
count = 0
for tweet in public_tweets:
  status_id = tweet.id
  text = tweet.text.encode('ascii',errors='ignore')
  text = re.sub("'", '', text)
  
  author_id = tweet.author.id
  retweet_count = tweet.retweet_count
  geo = tweet.geo
  created_at = tweet.created_at
  
  place = ''
  try:
    place = tweet.place.full_name
  except:
    place = tweet.place
  
  in_reply_to_status_id = tweet.in_reply_to_status_id
  in_reply_to_user_id = tweet.in_reply_to_user_id
  print("<=======================>")
  print(status_id) 
  print(text) 
  print(author_id) 
  print(retweet_count) 
  print(geo) 
  print(created_at) 
  print(place) 
  print(in_reply_to_status_id) 
  print(in_reply_to_user_id) 
  insert_status_query = "INSERT INTO home_status VALUES ({0}, '{1}', {2}, {3}, '{4}', '{5}'::timestamp, '{6}', '{7}', '{8}');".format(status_id, text, author_id, retweet_count, geo, created_at, place, in_reply_to_status_id, in_reply_to_user_id)
  try:
    cursor.execute(insert_status_query)
  except Exception as e:
    print("Cannot insert")
    print(e)
  count += 1
print(count)
print("<----->")

