import os
import uuid
from datetime import datetime

import boto3
from flask import Flask, request, jsonify
from sum_pairs import find_all_equal_sum_pairs

# Instead of hardcoding, read from environment variables (populated from a ConfigMap in Kubernetes)
DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME", "requests-log-table")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# Initialize AWS DynamoDB resource
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True  # Enable pretty JSON output

@app.route("/assignment", methods=["GET"])
def assignment():
    """
    POST /assignment
    Expects JSON input: { "data": [ ... ] }
    Returns JSON object in the format:
    {
        "results": [
            { "pairs": [ ... ], "sum": ... }
        ]
    }
    """
    data = request.get_json(force=True)
    arr = data.get("data", [])

    # Validate that 'arr' is a list of integers
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return jsonify({"error": "Input must be JSON with 'data' as a list of integers."}), 400

    # Log the input to standard output (Flask logger)
    app.logger.info(f"Received data: {arr}")

    # Generate a unique request ID and current timestamp
    request_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    # Log the request into DynamoDB (including the original input)
    try:
        table.put_item(
            Item={
                "requestId": request_id,
                "timestamp": timestamp,
                "requestPayload": arr  # Logging the input array
            }
        )
    except Exception as e:
        app.logger.error(f"Failed to log request to DynamoDB: {str(e)}")
        return jsonify({"error": f"Failed to log request to DynamoDB: {str(e)}"}), 500

    # Process the sum pairs
    pairs_by_sum = find_all_equal_sum_pairs(arr)

    # Transform the result
    results = [
        {"pairs": pairs, "sum": sum_value}
        for sum_value, pairs in pairs_by_sum.items()
    ]

    return jsonify({"results": results}), 200

if __name__ == "__main__":
    # If run locally for testing, it listens on 0.0.0.0:5001
    app.run(host="0.0.0.0", port=5000, debug=True)
