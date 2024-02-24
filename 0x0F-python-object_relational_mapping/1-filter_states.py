#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host = "localhost",
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3],
        port = 3306
    )
    cur = db.cursors()
    cur.execute("SELECT * FROM states WHRER name  LIKE BINARY '%N' ORDER BY states.id")
    rows = cur.fetcall()
    for row in rows:
        print(row)
    cur.close()
    db.close()