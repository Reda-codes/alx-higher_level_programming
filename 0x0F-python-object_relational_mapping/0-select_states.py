#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    db.close()