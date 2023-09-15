#!/usr/bin/python3
"""
Write_a script_that_accepts arguments_and_shows all_values in the_states
table_of_hbtn_0e_0_usa where_name matches_the_argument.
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
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == argv[4]]
