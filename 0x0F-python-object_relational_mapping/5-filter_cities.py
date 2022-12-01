#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = db.cursor()
    arg = [sys.argv[4]]
    c.execute("""SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id=states.id
            WHERE states.name=%s""", arg)
    query_rows = c.fetchall()
    result = ()
    for row in query_rows:
        result += (row)
    print(', '.join(result))
    c.close()
    db.close()
