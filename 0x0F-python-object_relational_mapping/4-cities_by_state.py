#!/usr/bin/python3
""" Module the connects to database and
queries the database"""

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3], port=3306)
cur = db.cursor()
cur.execute('SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON \
            states.id = cities.state_id ORDER BY id ASC')
rows = cur.fetchall()

i = 0
while(i < len(rows)):
    print(rows[i])
    i = i + 1

db.close()
