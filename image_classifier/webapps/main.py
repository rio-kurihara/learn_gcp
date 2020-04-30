import json

import requests
from flask import request, render_template

from flask import Flask

app = Flask(__name__, static_url_path="")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    response = requests.post('**URL**')
    response = response.content.decode()
    response = eval(response)
    label = response['label']
    # label = "aaa"

    return render_template('results.html', message=label)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
