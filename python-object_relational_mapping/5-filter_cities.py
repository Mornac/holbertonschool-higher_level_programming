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
    if len(sys.argv) != 5:
        sys.exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_searched = sys.argv[4]

    if "'" in state_searched:
        sys.exit()

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
        SELECT cities.name FROM cities INNER JOIN states
        ON states.id = cities.state_id
        WHERE states.name = '{}' ORDER BY cities.id ASC
    """.format(state_searched))
    query_rows = cur.fetchall()

    if len(query_rows) > 0:
        for row_num in range(len(query_rows)):
            if row_num != len(query_rows) - 1:
                print(query_rows[row_num][0], end=", ")
            else:
                print(query_rows[row_num][0])
    else:
        print()
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
