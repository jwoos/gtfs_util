#!/usr/bin/env python3

from contextlib import contextmanager

from gtfs_util.static.models import *
from gtfs_util.static import file

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgres+psycopg2://user:password@localhost:5432/tracksit')

Session = sessionmaker(bind=engine)
session = Session()


@contextmanager
def session_scope():
    session = Session()

    try:
        yield session
    finally:
        session.close()


base.Base.metadata.create_all(engine)

filename = 'data/static/subways.zip'
# filename = input('Enter the zip file name: ')

with session_scope() as session:
    for chunk in file.load_iter(filename, model=True, chunk_size=100):
        data = [x[0] for x in chunk]
        print(f'Adding {data}')
        session.add_all(data)
        session.commit()
