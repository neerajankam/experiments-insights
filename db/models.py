from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

from .connection import Database


Base = declarative_base()


class Insights(Base):
    """
    Represents the VIN table in the database.
    """

    __tablename__ = "insights"

    user_id = Column(String(17), primary_key=True)
    insights = Column(Text(255))


# Create the tables
Base.metadata.create_all(bind=Database.get_engine())
