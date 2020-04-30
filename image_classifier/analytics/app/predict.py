import numpy as np
from analytics.app.model import model_build

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


def predict(img):
    model = model_build()
    model.load_weights(
        '/home/work/image_classifier/analytics/app/models/weight.hdf5')
    predictions = model.predict(img)
    label = np.argmax(predictions[0])
    label_name = class_names[label]
    return label_name
