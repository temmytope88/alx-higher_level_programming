#!/usr/bin/python3
""" A module that quaries a
database using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
