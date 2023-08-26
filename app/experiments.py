import pandas as pd
from collections import defaultdict
from collections import Counter
import json

from db.connection import Database
from db.models import Insights as InsightsDB
from db.schema import InsightsSchema


class UserExperiments:
    def __init__(self):
        self.users_df = pd.read_csv("data/users.csv", sep=",", escapechar="\t")
        self.users_dict = self.users_df.to_dict(orient="records")

        self.compounds_df = pd.read_csv("data/compounds.csv", sep=",", escapechar="\t")
        self.compounds_dict = self.compounds_df.to_dict(orient="records")

        self.user_experiments_df = pd.read_csv(
            "data/user_experiments.csv", sep=",", escapechar="\t"
        )
        self.user_experiments = self.user_experiments_df.to_dict(orient="records")

    def get_user_experiments_mapping(self):
        user_experiments_mapping = defaultdict(list)
        for record in self.user_experiments:
            user_id = record["user_id"]
            user_experiments_mapping[user_id].append(record)
        return user_experiments_mapping

    def get_users_experiments(self):
        user_experiments_mapping = self.get_user_experiments_mapping()
        user_experiments_total = Counter()
        for user_id, experiments in user_experiments_mapping.items():
            user_experiments_total[user_id] = len(experiments)
        return user_experiments_total

    def get_experiments_count(self):
        return len(self.user_experiments)

    def get_users_count(self):
        return len(self.get_users())

    def get_users(self):
        return self.users_df["user_id"].to_list()

    def get_most_common_compound(self):
        compound_counter = Counter()
        for experiment in self.user_experiments:
            compound_ids = experiment["experiment_compound_ids"].split(";")
            for compound_id in compound_ids:
                compound_counter[compound_id] += 1
        return compound_counter.most_common()[0][0]

    def get_users_most_common_compound(self):
        user_compounds_mapping = self.get_user_compounds_mapping()
        user_most_common_compound_mapping = {
            record: max(value, key=value.count)
            for record, value in user_compounds_mapping.items()
        }

        return user_most_common_compound_mapping

    def get_user_compounds_mapping(self):
        user_experiments_mapping = defaultdict(list)
        for record in self.user_experiments:
            user_id = record["user_id"]
            compounds = record["experiment_compound_ids"].split(";")
            user_experiments_mapping[user_id].extend(compounds)
        return user_experiments_mapping

    def get_insights(self):
        with Database.get_session() as db_session:
            results = db_session.query(InsightsDB).all()
            results = InsightsSchema().dump(results, many=True)
        return results

    def delete_insights(self):
        with Database.get_session() as db_session:
            results = db_session.query(InsightsDB).delete()
            db_session.commit()

    def perform_etl(self):
        user_experiments = self.get_users_experiments()

        users_most_common_compound = self.get_users_most_common_compound()

        insights = {}
        users = self.get_users()
        experiments_count = self.get_experiments_count()

        with Database.get_session() as db_session:
            for user_id in users:
                insights[user_id] = {
                    "total_experiments": user_experiments.get(user_id, 0),
                    "average_num_experiments": user_experiments.get(user_id, 0)
                    / experiments_count,
                    "most_common_compound": users_most_common_compound.get(user_id),
                }
                db_session.add(
                    InsightsDB(user_id=user_id, user_insights=insights[user_id])
                )
            db_session.commit()
