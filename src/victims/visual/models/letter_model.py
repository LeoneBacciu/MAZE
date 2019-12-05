import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    from keras import Sequential
    from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout
    from keras import backend as K


def getLModel(dims):
    if K.image_data_format() == 'channels_first':
        input_shape = (3, dims[0], dims[1])
    else:
        input_shape = (dims[0], dims[1], 3)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), strides=(2, 2), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), strides=(2, 2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(.2))
    model.add(Dense(4, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
