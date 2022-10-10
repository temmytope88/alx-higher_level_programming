#!/usr/bin/python3
""" A module that quaries a
database using sqlalchemy"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'
    .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

stmt = select([State])
print(stmt)
result = engine.execute(stmt).fetchone()
if(result):
    print("{}: {}".format(result[0], result[1]))
else:
    print("")
