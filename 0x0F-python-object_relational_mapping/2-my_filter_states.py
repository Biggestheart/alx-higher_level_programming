#!/usr/bin/python3
"""
 Accepts_an_argument_and shows_all values in_the states_table_of
hbtn_0e_0_usa_where name_matches_the_argument.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT *\
                FROM `states` WHERE BINARY `name` = '{}'".format(argv[4]))
    [print(state) for state in cur.fetchall()]
