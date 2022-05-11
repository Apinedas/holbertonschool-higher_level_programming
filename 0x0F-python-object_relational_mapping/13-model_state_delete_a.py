#!/usr/bin/python3
'''
List found state from hbtn_0e_6_usa
'''


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import Session
    import sys

    engine = create_engine("mysql+pymysql://{}:{}@localhost/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()

    metadata = MetaData()

    Base.metadata.create_all(engine)
    session = Session(engine)

    found = []

    for state in session.query(State).order_by(State.id).all():
        if "a" in state.name:
            found.append(state)
    
    for del_state in found:
        session.delete(del_state)
        session.commit()

    session.close()
