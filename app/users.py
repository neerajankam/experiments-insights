import pandas as pd


class Users:
    users_df = pd.read_csv("data/users.csv", sep=",", escapechar="\t")
    users_dict = users_df.to_dict(orient="records")

    @classmethod
    def get_users(cls):
        return cls.users_df["user_id"].to_list()

    @classmethod
    def get_userids_names_mapping(cls):
        mappings = {}
        for user_record in cls.users_dict:
            user_id = user_record["user_id"]
            user_name = user_record["name"]
            mappings[user_id] = user_name
        return mappings
