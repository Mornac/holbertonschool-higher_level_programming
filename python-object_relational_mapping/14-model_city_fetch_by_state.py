#!/usr/bin/python3
"""
Module containing function listing objects from a database.
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


if __name__ == "__main__":
    """
    Lists City objects from a database.
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
    Session = sessionmaker(bind=engine)

    session = Session()

    # Get th state name
    cities = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
        )

    # Print the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
