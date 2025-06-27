#!/usr/bin/python3
"""
Module that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
# import pymysql
# pymysql.install_as_MySQLdb()
import MySQLdb
import sys


def main():
    if len(sys.argv) != 5:
        sys.exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched_state = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY id ASC"
        .format(searched_state)
    )
    query_roows = cur.fetchall()
    for row in query_roows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
