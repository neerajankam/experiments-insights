from flask import Flask, request, jsonify

from experiments import UserExperiments

user_experiments = UserExperiments()
app = Flask(__name__)


@app.route("/insights", methods=["POST", "GET", "DELETE"])
def trigger_etl():
    if request.method == "POST":
        user_experiments.perform_etl()
        return jsonify({"message": "ETL process started"}), 200
    elif request.method == "GET":
        return jsonify(user_experiments.get_insights())
    elif request.method == "DELETE":
        user_experiments.delete_insights()
        return jsonify({"message": "Successfully deleted insights"}), 200


@app.route("/compounds", methods=["GET"])
def get_compounds():
    print(user_experiments.compounds_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
