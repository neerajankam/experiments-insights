import pandas as pd

from collections import defaultdict
from collections import Counter


class Compounds:
    compounds_df = pd.read_csv("data/compounds.csv", sep=",", escapechar="\t")
    compounds_dict = compounds_df.to_dict(orient="records")
    user_experiments_df = pd.read_csv(
        "data/user_experiments.csv", sep=",", escapechar="\t"
    )
    user_experiments = user_experiments_df.to_dict(orient="records")

    @classmethod
    def get_most_common_compound(cls, experiments):
        compound_counter = Counter()

        for experiment in experiments:
            compound_ids = experiment["experiment_compound_ids"].split(";")
            for compound_id in compound_ids:
                compound_counter[compound_id] += 1

        return compound_counter.most_common()[0][0]

    @classmethod
    def get_user_compounds_mapping(cls):
        user_experiments_mapping = defaultdict(list)
        for record in cls.user_experiments:
            user_id = record["user_id"]
            compounds = record["experiment_compound_ids"].split(";")
            user_experiments_mapping[user_id].extend(compounds)
        return user_experiments_mapping

    @classmethod
    def get_users_most_common_compound(cls):
        user_compounds_mapping = cls.get_user_compounds_mapping()
        user_most_common_compound_mapping = {
            record: max(value, key=value.count)
            for record, value in user_compounds_mapping.items()
        }

        return user_most_common_compound_mapping

    @classmethod
    def get_compound_ids_names_mapping(cls):
        mappings = {}
        for user_record in cls.compounds_dict:
            compound_id = str(user_record["compound_id"])
            compound_name = user_record["compound_name"]
            mappings[compound_id] = compound_name
        return mappings
