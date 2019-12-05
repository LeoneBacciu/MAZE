from json import loads
from models.letter_model import getLModel
from models.color_model import getCModel
from keras_preprocessing.image import ImageDataGenerator

json = open('config.json', 'r').read()
data = loads(json)
data = data['training']

dims = tuple(data['model']['input'])
batch_size = data['model']['b_size']
name = data['model']['name']
categories = ["green", "red", "white", "yellow"] if name == 'color' else ['h', 'n', 's', 'u']

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)
pred_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    data['directory']+'/'+name+'/train',
    classes=categories,
    target_size=dims,
    batch_size=batch_size,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    data['directory']+'/pred',
    classes=categories,
    target_size=dims,
    batch_size=batch_size,
    class_mode='categorical')

model = None
if name == 'color':
    model = getCModel(dims)
else:
    model = getLModel(dims)

if data['model']['trained']:
    model.load_weights('weights/'+name+'.h5')

model.fit_generator(
    train_generator,
    steps_per_epoch=data['samples'][0] // batch_size,
    epochs=data['model']['epochs'],
    validation_data=validation_generator,
    validation_steps=data['samples'][1] // batch_size)
model.save_weights('weights/'+name+'.h5')
