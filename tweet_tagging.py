from __future__ import absolute_import, print_function 
import psycopg2
import psycopg2.extras
import sys
import re

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
  cursor.execute("SELECT id, text FROM home_status WHERE interesting IS NULL ORDER BY id ASC")
  rows = cursor.fetchall()
except Exception as e:
  print("Cannot get texts")
  print(e)


count = 0
for row in rows:
  tweet_id = row[0] 
  text = row[1]
  tag = raw_input("ID = " + str(tweet_id) + " TWEET : " + text + " = ") 
  print(tag) 
  
  insert_string = "UPDATE home_status SET interesting = '{0}' WHERE id = {1} ".format(tag, tweet_id) 
  print(insert_string)
  try:
    cursor.execute(insert_string)
  except Exception as e:
    print("Cannot insert")
    print(e)
  count += 1
print(count)
print("<----->")

