# REST API - Multi-Action Version
from flask import Flask, request, jsonify
from verdict_engine import evaluate_action

app = Flask(__name__)

@app.route('/evaluate_multi', methods=['POST'])
def evaluate_multi():
    data = request.get_json()
    actions = data.get("actions", [])
    metadata = data.get("metadata", {})

    if not actions or not isinstance(actions, list):
        return jsonify({"error": "A list of actions must be provided"}), 400

    results = []
    for action in actions:
        verdict = evaluate_action(action, metadata)
        results.append(verdict)

    return jsonify({"evaluations": results})

if __name__ == "__main__":
    app.run(debug=True)
