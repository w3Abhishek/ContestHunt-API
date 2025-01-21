from flask import Flask, jsonify, render_template
from flask_cors import CORS
from dbmanager import fetch_items
import os

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contests")
def get_contests():
    return jsonify({"data": fetch_items("contests")})

@app.route("/hackathons")
def get_hackathons():
    return jsonify({"data": fetch_items("hackathons")})

@app.route("/bounties")
def get_bounties():
    return jsonify({"data": fetch_items("bounties")})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)