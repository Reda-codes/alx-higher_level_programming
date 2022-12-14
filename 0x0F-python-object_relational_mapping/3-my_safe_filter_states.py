#!/usr/bin/python3
"""
script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
that is safe from MySQL injections!
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = db.cursor()
    arg = [sys.argv[4]]
    c.execute(
            """SELECT * FROM states
            WHERE NAME=%s ORDER BY id ASC""", [sys.argv[4]])
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    db.close()
