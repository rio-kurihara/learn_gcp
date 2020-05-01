import numpy as np
from app.network import build

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


class Classifier:
    def __init__(self, weight_path):
        self.model = build()
        self.model.load_weights(weight_path)

    def predict(self, img):
        predictions = self.model.predict(img)
        label = np.argmax(predictions[0])
        label_name = class_names[label]
        return label_name
