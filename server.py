from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": "*"}})

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    query_text = data.get("query", "")
    if not query_text:
        return jsonify({"response": "Invalid query"}), 400

    result = subprocess.run(["python", "query_data.py", query_text], capture_output=True, text=True)
    response_text = result.stdout.strip().split("Response:")[-1].strip() if "Response:" in result.stdout else "Error processing query"

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
