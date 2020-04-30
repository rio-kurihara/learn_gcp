import base64
import json

import requests
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="")

# load config
with open('./setting/webapp.json', 'r') as f:
    config = json.load(f)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
        # 画像として読み込み
        stream = request.files.get('image')
        img_byte = stream.read()
        img_base64 = base64.b64encode(img_byte)
        img_str = img_base64.decode('utf-8')

        data = {'img': img_str}
        response = requests.post(
            config['backend_URL'], json=json.dumps(data))

        response = response.content.decode()
        response = eval(response)
        label = response['label']

    return render_template('results.html', message=label)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
