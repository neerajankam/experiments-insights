from flask import Flask

from experiments import UserExperiments

app = Flask(__name__)
user_experiments = UserExperiments()


@app.route("/insights", methods=["GET"])
def trigger_etl():
    user_experiments.perform_etl()
    return {"message": "ETL process started"}, 200


@app.route("/compounds", methods=["GET"])
def get_compounds():
    print(user_experiments.compounds_dict)


if __name__ == "__main__":
    app.run(debug=True)
    # user_experiments.perform_etl()
    # get_compounds()
