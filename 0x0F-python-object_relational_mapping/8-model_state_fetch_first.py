#!/usr/bin/python3
""" A module that quaries a
database using sqlalchemy"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).first()
    if(result):
        print("{}: {}".format(result.id, result.name))
    else:
        print("")

    session.close()
