#!/usr/bin/python3
""" A module that quaries a
database using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                       format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()
value = sys.argv[4]
results = session.query(State.id).filter
(State.name == value).order_by(State.id)
if results:
    for result in results:
        print("{}".format(result[0]))
else:
    print("Not found")
