from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path="")


@app.route('/', methods=['POST'])
def post():
    response = jsonify({'label': 'TEST'})
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
