# REST API - Single Action Version
from flask import Flask, request, jsonify
from verdict_engine import evaluate_action

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    action = data.get("action")
    metadata = data.get("metadata", {})

    if not action:
        return jsonify({"error": "No action provided"}), 400

    verdict = evaluate_action(action, metadata)
    return jsonify(verdict)

if __name__ == "__main__":
    app.run(debug=True)
