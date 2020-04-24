from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
import cv2
from image_process import canny
from datetime import datetime
import os
import string
import random
from google.cloud import storage

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
        app.root_path, 'keras-tutorial-274304-8b2b89137ac6.json')
    storage_client = storage.Client.from_service_account_json(p)
    bucket = storage_client.get_bucket('keras-tutorial-274304.appspot.com')

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

        # save_path = os.path.join(SAVE_DIR, dt_now + ".png")
        # cv2.imwrite(save_path, img)

        # GCSに保存
        blob = bucket.blob(dt_now + '.png')
        # blob.upload_from_string(
        #     stream.read(), content_type=stream.content_type)
        blob.upload_from_filename(temp_local_filename)

        # os.remove(temp_local_filename)

        return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
