#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Description:
#   This application is used to discovery databases in PostgeSQL Cluster.
#
# Author: Przemyslaw Ciesielski <przemyslaw.ciesielski@gmail.com>
#

import psycopg2
import json

try:
  conn = psycopg2.connect("dbname='template1' user='postgres' password=''")
except:
  print "I am unable to connect to the database"

cur = conn.cursor()
try:
  cur.execute("""SELECT datname from pg_database WHERE datistemplate = false AND datname <> 'postgres'""")
except:
  print "Can't get db names!"

dbnames = []
rows = cur.fetchall()
for row in rows:
  dbnames += [{'{#DBNAME}':row[0]}]

print json.dumps({'data':dbnames},sort_keys=True,indent=7,separators=(',',':'))







                              #import commands
                              #import os
                              #import sys
                              #import json
                              #from optparse import OptionParser




                              # echo -n '{"data":['

                              # for i in $(echo "select datname FROM pg_database WHERE datistemplate = false;" | psql -U postgres -tA); do
                              #   echo -n "{\"{#DBNAME}\":\"$i\"},"
                              #   done

                               #  echo -e ']}'

