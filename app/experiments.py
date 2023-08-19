import pandas as pd
from collections import defaultdict
from collections import Counter

from db.connection import Database
from db.models import Insights as InsightsDB


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

    def get_user_experiments_total(self):
        user_experiments_mapping = self.get_user_experiments_mapping()
        user_experiments_total = Counter()
        for user_id, experiments in user_experiments_mapping.items():
            user_experiments_total[user_id] = len(experiments)
        return user_experiments_total

    def get_total_experiments(self):
        return len(self.user_experiments)

    def get_total_users(self):
        return len(self.users_df.index)

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

    def perform_etl(self):
        """
        Total experiments a user ran.
        Average experiments amount per user.
        User's most commonly experimented compound.
        """

        # 1. Total experiments a user ran.
        user_experiments_total = self.get_user_experiments_total()
        print(user_experiments_total)

        # 2. Average experiments amount per user.
        total_experiments = self.get_total_experiments()
        total_users = self.get_total_users()
        average_num_experiments_per_user = total_experiments / total_users
        print(total_experiments, total_users, average_num_experiments_per_user)

        # 3. User's most commonly experimented compound.
        users_most_common_compound = self.get_users_most_common_compound()
        print(users_most_common_compound)

        db_session = Database.get_session()
        print(db_session.query(InsightsDB).all())
