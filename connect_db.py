#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

conn = psycopg2.connect("dbname='ml_projects' user='yahyaeru' host='localhost' password='secret'")
