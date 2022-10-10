#!/usr/bin/python3
""" Module the connects to database and
queries the database where name is an
argument safe of SQL injection"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3], port=3306)
    cur = db.cursor()
    value = sys.argv[4]
    cur.execute("""SELECT * FROM states
                WHERE name = '%s'
                ORDER BY 'id' ASC""" % (value,))
    rows = cur.fetchall()

    i = 0
    while(i < len(rows)):
        print(rows[i])
        i = i + 1

    cur.close()
    db.close()
