#!/usr/bin/python3
"""
Module that lists aull cities of a specific state
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """
    function that takes in the name of a state
    as an argument
    and lists all cities of the state
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

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
        "SELECT * FROM cities"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
