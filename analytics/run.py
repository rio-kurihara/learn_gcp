import base64
import json

import cv2
import numpy as np

from app.model import Classifier
from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path="")

# load config
with open('./setting/analytics.json', 'r') as f:
    config = json.load(f)


@app.route('/', methods=['POST'])
def post():
    json_data = request.get_json()  # POSTされたjsonを取得
    dict_data = json.loads(json_data)  # jsonを辞書に変換

    img = dict_data["img"]  # base64を取り出す # str
    img = base64.b64decode(img)  # base64に変換された画像データを元のバイナリデータに変換 # bytes
    img_arr = np.asarray(bytearray(img), dtype=np.uint8)
    img_cv2 = cv2.imdecode(img_arr, -1)  # 'load it as it is'

    # predict
    model = Classifier(config['weight_path'])
    img_scaled = img_cv2 / 255.0
    img_scaled = (np.expand_dims(img_scaled, 0))
    pred_label = model.predict(img_scaled)

    response = jsonify({'label': pred_label})
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
