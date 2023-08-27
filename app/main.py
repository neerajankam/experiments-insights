from flask import Flask, request, jsonify

from insights import Insights

insights_cls = Insights()
app = Flask(__name__)


@app.route("/insights", methods=["POST", "GET", "DELETE"])
def trigger_etl():
    if request.method == "POST":
        insights_cls.perform_etl()
        return jsonify({"message": "ETL process started"}), 200
    elif request.method == "GET":
        return jsonify(insights_cls.get_insights())
    elif request.method == "DELETE":
        insights_cls.delete_insights()
        return jsonify({"message": "Successfully deleted insights"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
