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
rows = None 

try:
  cursor.execute("SELECT author_id FROM home_status WHERE author_id NOT IN (SELECT id FROM home_author) GROUP BY author_id;")
  rows = cursor.fetchall()
except Exception as e:
  print("Cannot get id")
  print(e)

count = 0
for row in rows:
  author_id = row[0]
  print("------------")
  print("author_id = " + str(author_id))
  author_data = api.get_user(author_id)
  
  author_screen_name = author_data.screen_name 
  author_name = author_data.name.encode('ascii',errors='ignore') 
  author_name = re.sub("'", '', author_name)

  author_verified = author_data.verified
  author_protected = author_data.protected
  author_location = author_data.location.encode('ascii',errors='ignore')  
  author_location = re.sub("'", '', author_location)
  
  author_language = author_data.lang 
  author_description = author_data.description.encode('ascii',errors='ignore') 
  author_description = re.sub("'", '', author_description)
  
  author_geo_enabled = author_data.geo_enabled 
  author_time_zone = author_data.time_zone 
  author_created_at = author_data.created_at 
  
  author_followers_count = author_data.followers_count
  author_friends_count = author_data.friends_count 
  author_statuses_count = author_data.statuses_count 
  author_favourites_count = author_data.favourites_count 
  author_listed_count = author_data.listed_count

  print(str(author_id) + "=" + author_screen_name + "count = " + str(count))
  insert_status_query = "INSERT INTO home_author VALUES ({0}, {1}, {2}, {3}, '{4}', {5}, '{6}', {7}, {8}, '{9}', '{10}', {11}, '{12}', '{13}'::timestamp, '{14}', {15});".format(author_id, author_verified, author_followers_count, author_protected, author_location, author_statuses_count, author_description,author_friends_count, author_geo_enabled, author_screen_name, author_language, author_favourites_count, author_name,
author_created_at, author_time_zone, author_listed_count)

  try:
    cursor.execute(insert_status_query)
  except Exception as e:
    print("Cannot insert")
    print(e)
  count += 1
print(count)
print("<----->")

