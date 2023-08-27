import pandas as pd
from collections import defaultdict
from collections import Counter


class Experiments:
    user_experiments_df = pd.read_csv(
        "data/user_experiments.csv", sep=",", escapechar="\t"
    )
    user_experiments = user_experiments_df.to_dict(orient="records")

    @classmethod
    def get_user_experiments_mapping(cls):
        user_experiments_mapping = defaultdict(list)
        for record in cls.user_experiments:
            user_id = record["user_id"]
            user_experiments_mapping[user_id].append(record)
        return user_experiments_mapping

    @classmethod
    def get_users_experiments(cls):
        user_experiments_mapping = cls.get_user_experiments_mapping()
        user_experiments_total = Counter()
        for user_id, experiments in user_experiments_mapping.items():
            user_experiments_total[user_id] = len(experiments)
        return user_experiments_total

    @classmethod
    def get_experiments_count(cls):
        return len(cls.user_experiments)
