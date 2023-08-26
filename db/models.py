from sqlalchemy import Column, Integer, String, JSON, text
from sqlalchemy.ext.declarative import declarative_base

from .connection import Database


Base = declarative_base()


class Insights(Base):
    """
    Represents the VIN table in the database.
    """

    __tablename__ = "insights"

    user_id = Column(String(17), primary_key=True)
    user_insights = Column(JSON)


import psycopg2
import time

while True:
    if Database.wait_for_database():
        break
# Create the tables
Base.metadata.create_all(bind=Database.get_engine())
