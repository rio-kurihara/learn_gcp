# -*- encoding: UTF-8 -*-
import json
# from analytics.app import app
from flask import jsonify, request
import numpy as np
import cv2
from app import model
from flask import Flask

app = Flask(__name__, static_url_path="")


@app.route('/')
def test():
    return 'TEST'


@app.route('/upload', methods=['POST'])
def post():

    if request.files['image']:
        # 画像として読み込み
        stream = request.files.get('image')
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 0)

        # predict
        img_scaled = img / 255.0
        img_scaled = (np.expand_dims(img_scaled, 0))
        pred_label = predict(img_scaled)
        response = jsonify({'class': pred_label})
    return response
