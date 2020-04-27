from tensorflow import keras
from model import model_build

# load data
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images,
                               test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0

# train
model = model_build()
model.fit(train_images, train_labels, epochs=5)
model.save_weights('../models/weight.hdf5')
