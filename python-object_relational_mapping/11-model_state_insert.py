#!/usr/bin/python3
"""
Module to add specific object to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Adds a State object in a database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)

    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    state = session.query(State).where(
        State.name == "Louisiana"
    ).limit(1).one()

    print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    main()
