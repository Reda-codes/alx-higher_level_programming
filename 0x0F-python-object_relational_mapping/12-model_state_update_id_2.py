#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                 sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    session.query(State).filter(State.id == 2).update(
            {State.name: "New Mexico"}, synchronize_session=False)
    session.commit()
    session.close()
