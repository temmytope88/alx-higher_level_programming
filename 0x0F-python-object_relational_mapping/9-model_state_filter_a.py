#!/usr/bin/python3
""" A module that quaries a
database using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1],
                sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).\
    filter(State.name.like('%a%')).order_by(State.id)


    for result in results:
        print("{}: {}".format(result.id, result.name))

    session.close()
