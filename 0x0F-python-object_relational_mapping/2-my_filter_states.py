#!/usr/bin/python3
""" Module the connects to database and
queries the database where name is an
argument"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306, charset='utf8')
    cur = db.cursor()
    value = sys.argv[4]
    cur.execute("""SELECT * FROM states
                WHERE states.name = '{:s}'
                ORDER BY id ASC""".format(value))
    rows = cur.fetchall()

    i = 0
    while(i < len(rows)):
        if rows[i][1] == value:
            print(rows[i])
        i = i + 1
    db.close()
