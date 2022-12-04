#!/usr/bin/python3
"""
script that creates the State “California”
with the City “San Francisco” from
the database hbtn_0e_100_usa
"""
import sys
from relationship_city import Base, State, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                 sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)
    new_state = State(name='California')
    session.commit()
    new_city = City(name='San Francisco', state=new_state)
    session.add(new_city)
    session.add(new_state)
    session.commit()
    session.close()    
