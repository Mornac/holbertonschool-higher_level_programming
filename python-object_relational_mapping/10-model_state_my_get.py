#!/usr/bin/python3
"""
Module containing function displaying specific objects from a database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


def main():
    """
    Prints State object matching argument from a database.
    """
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_searched = sys.argv[4]

    if "'" in state_searched:
        sys.exit(2)

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

    try:
        state = (
            session.query(State)
            .filter(State.name == state_searched)
            .order_by(State.id)
            .limit(1)
            .one()
        )
    except NoResultFound:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    main()
