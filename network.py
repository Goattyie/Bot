import numpy as np
import tensorflow as tf

from tensorflow import keras as k




def machine_learning():   #обучение
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = k.utils.normalize(x_train, axis = 1)
    x_test = k.utils.normalize(x_test, axis = 1)

    x_train = x_train.reshape((60000, 28, 28, 1))
    x_test = x_test.reshape((10000, 28, 28, 1))

    model = k.Sequential([
                     k.layers.Conv2D(64,(3,3),activation='relu', input_shape=(28,28,1)),
                     k.layers.MaxPool2D((2,2)),
                     k.layers.Flatten(),
                     k.layers.Dense(64, activation=tf.nn.relu),
                     k.layers.Dense(10, activation=tf.nn.softmax)])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
    model.fit(x_train, y_train, epochs=3)
    model.save('epic_num_reader.model')
    
def processing():
    model = k.models.load_model('epic_num_reader.model')#загрузка обученной модели
    result = model.predict(picture) #итоговая цифра/ picture - массив типа [1,1,28,28] //количество картинов, кол-во цветовых каналов и размеры