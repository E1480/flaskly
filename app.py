from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def _root():
    return jsonify({"status":"OK"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PROT", 5000)))
