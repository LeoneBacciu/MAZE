from json import loads

import cv2
import numpy as np
from models.letter_model import getLModel
from models.color_model import getCModel
from utils.recorder import Camera
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=FutureWarning)
    from keras_preprocessing.image import ImageDataGenerator


json = open('config.json', 'r').read()
data = loads(json)
dims = tuple(data['training']['model']['input'])
data = data['predicting']

directory = data['directory']
name = data['model']
categoriesC = ["green", "red", "white", "yellow"]
categoriesL = ['h', 'n', 's', 'u']

cam = Camera(0)

pred_datagen = ImageDataGenerator(rescale=1. / 255)
pred_gen = pred_datagen.flow_from_directory(
    directory,
    shuffle=False,
    batch_size=1,
    target_size=dims
)

model = None
model2 = None
if name == 'color':
    model = getCModel(dims)
    model.load_weights('weights/' + name + '.h5')
elif name == 'letter':
    model = getLModel(dims)
    model.load_weights('weights/' + name + '.h5')
else:
    model = getCModel(dims)
    model2 = getLModel(dims)
    model.load_weights('weights/color.h5')
    model2.load_weights('weights/letter.h5')


def predict(_, frame):
    cv2.imwrite(directory + '/f/f.png', frame)
    pred_gen.reset()
    pred = model.predict_generator(pred_gen, steps=1)
    p = int(np.where(pred[0] == np.amax(pred[0]))[0])
    if model2 and p == 2:  # if prediction == 'white'
        pred = model2.predict_generator(pred_gen, steps=1)
        p = int(np.where(pred[0] == np.amax(pred[0]))[0])
        print(categoriesL[p])
    elif name == 'letter':
        print(categoriesL[p])
    else:
        print(categoriesC[p])


cam.record(predict, 1000)
