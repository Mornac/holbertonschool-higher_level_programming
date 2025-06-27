#!/usr/bin/python3
"""
Module containing function updating specific object from a database.
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


if __name__ == "__main__":
    """
    Updates a State object from a database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )
    # create a configured class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # Update the state
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State object
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
