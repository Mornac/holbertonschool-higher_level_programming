#!/usr/bin/python3
"""
Module that contains a function to display specific objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    # arguments for the table
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_searched = sys.argv[4]

    # create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )

    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # create session
    session = Session()

    state = session.query(State).filter(State.name == state_searched).first()

    # print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
