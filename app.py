from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from dbmanager import fetch_items
import os

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<type>")
def get_items(type):
    platform = request.args.get("platform")
    items = fetch_items(type, platform)
    return jsonify(items)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)