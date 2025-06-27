#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
#import pymysql
#pymysql.install_as_MySQLdb()
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    """)
    query_roows = cur.fetchall()
    for row in query_roows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
