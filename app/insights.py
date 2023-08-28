import pandas as pd
from collections import defaultdict
from collections import Counter
import logging
import json
from sqlalchemy.exc import SQLAlchemyError

from db.connection import Database
from db.models import Insights as InsightsDB
from db.schema import InsightsSchema
from users import Users
from compounds import Compounds
from experiments import Experiments


class Insights:
    users = Users()
    compounds = Compounds()
    experiments = Experiments()

    @classmethod
    def perform_etl(cls):
        user_experiments = cls.experiments.get_users_experiments()
        users_most_common_compound = cls.compounds.get_users_most_common_compound()

        users = cls.users.get_users()
        user_ids_names_mapping = cls.users.get_userids_names_mapping()

        experiments_count = cls.experiments.get_experiments_count()
        compound_ids_names_mapping = cls.compounds.get_compound_ids_names_mapping()
        insights = {}

        try:
            with Database.get_session() as db_session:
                if cls.get_insights():
                    cls.delete_insights()
                for user_id in users:
                    user_name = user_ids_names_mapping[user_id]
                    compound_id = users_most_common_compound.get(user_id)
                    compound_name = compound_ids_names_mapping[compound_id]
                    insights[user_name] = {
                        "total_experiments": user_experiments.get(user_id, 0),
                        "average_num_experiments": user_experiments.get(user_id, 0)
                        / experiments_count,
                        "most_common_compound": compound_name,
                    }
                    db_session.add(
                        InsightsDB(
                            user_name=user_name, user_insights=insights[user_name]
                        )
                    )
                db_session.commit()
        except SQLAlchemyError:
            logging.exception("Error encountered while interacting with the database.")
            raise SQLAlchemyError(
                "Error encountered while interacting with the database."
            )
        except Exception:
            logging.exception("Error encountered while computing insights.")

    @classmethod
    def get_insights(cls):
        try:
            with Database.get_session() as db_session:
                results = db_session.query(InsightsDB).all()
                results = InsightsSchema().dump(results, many=True)
            return results
        except SQLAlchemyError:
            logging.exception("Error encountered while interacting with the database.")
            raise SQLAlchemyError(
                "Error encountered while interacting with the database."
            )

    @classmethod
    def delete_insights(cls):
        try:
            with Database.get_session() as db_session:
                results = db_session.query(InsightsDB).delete()
                db_session.commit()
        except SQLAlchemyError:
            logging.exception("Error encountered while interacting with the database.")
            raise SQLAlchemyError(
                "Error encountered while interacting with the database."
            )
