import io
import os
import random
import string
from datetime import datetime

import cv2
import numpy as np

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from google.cloud import storage
from image_process import canny
from PIL import Image

SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app = Flask(__name__, static_url_path="")


def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])


@app.route('/')
def index():
    return render_template('index.html', images=os.listdir(SAVE_DIR)[::-1])


@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(SAVE_DIR, path)

# 参考: https://qiita.com/yuuuu3/items/6e4206fdc8c83747544b
@app.route('/upload', methods=['POST'])
def upload():
    # settings
    p = os.path.join(
        app.root_path, 'key.json')
    storage_client = storage.Client.from_service_account_json(p)
    bucket = storage_client.get_bucket('***')

    if request.files['image']:
        # 画像として読み込み
        stream = request.files.get('image')
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # 変換
        img = canny(img)

        # 保存
        dt_now = datetime.now().strftime("%Y%m%d_%H%M%S_") + random_str(5)
        temp_local_filename = os.path.join(SAVE_DIR, dt_now + ".png")
        cv2.imwrite(temp_local_filename, img)

        # OpenCV -> PIL
        img_cv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_cv)
        # PIL -> Bytes
        output = io.BytesIO()
        img_pil.save(output, format='PNG')

        # save to GCS
        blob = bucket.blob(dt_now + '.png')
        blob.upload_from_string(
            output.getvalue(), content_type=stream.content_type)

        return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
