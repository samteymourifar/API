from flask import Flask, request, jsonify
from sum_pairs import find_all_equal_sum_pairs

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True  # Enable pretty JSON output

@app.route("/assignment", methods=["GET"])
def assignment():
    """
    POST /assignment
    Expects JSON input: { "data": [ ... ] }
    Returns JSON object in the format:
    { "results": [ { "pairs": [ ... ], "sum": ... } ] }
    """
    data = request.get_json(force=True)
    arr = data.get("data", [])

    # Validate that 'arr' is indeed a list of integers
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return jsonify({"error": "Input must be JSON with 'data' as a list of integers."}), 400

    # Find all sums with at least two distinct pairs
    pairs_by_sum = find_all_equal_sum_pairs(arr)

    # Transform the result into the required output format
    results = [
        {"pairs": pairs, "sum": sum_value}
        for sum_value, pairs in pairs_by_sum.items()
    ]

    # Return the results as JSON with pretty formatting
    return jsonify({"results": results}), 200

if __name__ == "__main__":
    # Runs the Flask app on http://0.0.0.0:5000/ by default when using Gunicorn
    app.run(host="0.0.0.0", port=5000, debug=True)