#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_city import City
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uri = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        uri.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
