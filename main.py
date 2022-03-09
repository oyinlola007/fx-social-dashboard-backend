import cogs.config as config
import cogs.db as db

from flask import Flask
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route("/api/v1/paid_affiliates",methods=['GET'])
def get_affiliate_paid():
    data = db.get_affiliate_paid()
    return {'data' : data, 'total' : db.get_sum_affiliate_paid()}, 200

@app.route("/api/v1/to_pay_affiliates",methods=['GET'])
def get_affiliate_to_pay():
    data = db.get_affiliate_to_pay()
    return {'data' : data, 'total' : db.get_sum_affiliate_to_pay()}, 200

@app.route("/api/v1/active_members",methods=['GET'])
def get_active_members():
    data = db.get_active_members()
    return {'data' : data}, 200

@app.route("/api/v1/on_trial",methods=['GET'])
def get_on_trial():
    data = db.get_on_trial()
    return {'data' : data}, 200

@app.route("/api/v1/leaderboard",methods=['GET'])
def get_leaderboard():
    data = db.get_leaderboard()
    return {'data' : data}, 200


if __name__ == '__main__':
    app.run(
        host='0.0.0.0'
    )