#!/usr/bin/python3
"""
Module containing function adding specific object from a database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Adds a State object in a database.
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    # create a new state
    new_state = State(name="Louisiana")

    # add the new state
    session.add(new_state)

    # commit the session to the database
    session.commit()

    # print the id of the new state
    print(new_state.id)

    session.close()
