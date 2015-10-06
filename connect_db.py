#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import psycopg2.extras
import sys

conn = psycopg2.connect("dbname='ml_projects' user='yahyaeru' host='localhost' password='secret'")

cursor = conn.cursor()
cursor.execute("INSERT INTO home_status VALUES (650370876307697664, 'omg idk', 74945420, 0, 'None', '2015-10-03 18:04:34'::timestamp, 'None');")

row_count = 0
for row in cursor:
	row_count += 1
	print "row: %s %s\n" % (row_count, row)
