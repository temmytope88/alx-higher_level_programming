#!/usr/bin/python3
""" Module the connects to database and
queries the database"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    value = sys.argv[4]
    if value:
        cur.execute("""SELECT cities.name
                    FROM cities JOIN states
                    ON states.id = cities.state_id
                    WHERE states.name = '{:s}'
                    ORDER BY cities.id ASC""".format(value))
        rows = cur.fetchall()

        i = 0
        count = len(rows) - 1
        while(i < len(rows)):
            if i == count:
                print(rows[i][0])
            else:
                print(rows[i][0], end=", ")
            i = i + 1

    cur.close()
    db.close()
