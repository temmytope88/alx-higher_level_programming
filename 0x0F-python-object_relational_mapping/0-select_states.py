#!/usr/bin/python3
""" Module the connects to database and
queries the database """
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3], port=3306, charset="utf8")
cur = db.cursor()
cur.execute('SELECT * FROM states ORDER BY id ASC')
rows = cur.fetchall()
s
i = 0
while(i < len(rows)):
    print(rows[i])
    i = i + 1

cur.close()
db.close()
