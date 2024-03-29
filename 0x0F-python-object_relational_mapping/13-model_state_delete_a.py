#!/usr/bin/python3
"""
deletes_all_state_objects with_a name_containing the_letter_a_from
the_database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like("%a%")).all():
        session.delete(state)
    session.commit()
    session.close()
