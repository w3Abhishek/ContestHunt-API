from flask import Flask, jsonify
from flask_cors import CORS
from dbmanager import fetch_items

app = Flask(__name__)

CORS(app)

@app.route("/contests")
def get_contests():
    return jsonify({"data": fetch_items("contests")})

@app.route("/hackathons")
def get_hackathons():
    return jsonify({"data": fetch_items("hackathons")})

@app.route("/bounties")
def get_bounties():
    return jsonify({"data": fetch_items("bounties")})