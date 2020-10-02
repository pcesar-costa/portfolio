import numpy as np
from tensorflow.keras import models

model = models.load_model('./model/ml_model.h5')

def transform_img(img_file):
    img = img_file.convert('RGB').resize((150,150))
    return np.asarray(img) / 255

def predict(img_file):
    data = transform_img(img_file)
    prediction = model.predict(np.asarray([data]))
    return np.argmax(prediction, axis=1)[0]