#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1]
        passwd=sys.argv[2]
        db=sys.argv[3]
        port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT name FROM states WHERE name = N% ORDER BY id ASC")
    query_roows = cur.fetchall()
    for row in query_roows:
        print(row)
    cur.close()
    db.close()
