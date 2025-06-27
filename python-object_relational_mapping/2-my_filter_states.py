#!/usr/bin/python3
"""
Module that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def main():
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(searched_state)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
