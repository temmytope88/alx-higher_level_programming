#!/usr/bin/python3
""" model for state class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ A class that inherits from
    declarative_base(sqlalchemy)

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
