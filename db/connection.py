import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from db.config import DATABASE_URL
from db.database_interface import DatabaseInterface


class Database(DatabaseInterface):
    """
    Singleton class for the database engine.

    Provides method to get a new session and access the engine.
    """

    __engine = None
    __session_factory = None

    @classmethod
    def check_database_connection(cls):
        """
        Checks if the database connection is ready.

        :return: True if the database is ready, False otherwise.
        :rtype: bool
        """
        try:
            engine = cls.get_engine()
            with engine.connect():
                return True
        except OperationalError:
            return False

    @classmethod
    def wait_for_database(cls):
        """
        Waits for the database to be ready.

        :return: None
        """
        while not cls.check_database_connection():
            print("Waiting for the database...")
            time.sleep(2)
        print("Database is ready!")
        return True

    @classmethod
    def get_session(cls):
        """
        Returns a new database session.

        :return: The database session.
        :rtype: SQLAlchemy session
        """
        cls.wait_for_database()

        if cls.__session_factory is None:
            cls.__session_factory = sessionmaker(bind=cls.get_engine())
        return cls.__session_factory()

    @classmethod
    def get_engine(cls):
        """
        Returns the database engine.

        :return: The database engine.
        :rtype: SQLAlchemy engine
        """
        if cls.__engine is None:
            cls.__engine = create_engine(DATABASE_URL)
        return cls.__engine
