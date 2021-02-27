import numpy as np
import tensorflow as tf

from tensorflow import keras as k
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array


def machine_learning():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test)=mnist.load_data()

    x_train = k.utils.normalize(x_train, axis=1)
    x_test = k.utils.normalize(x_test, axis=1)

    x_train = x_train.reshape((60000, 28, 28, 1))
    x_test = x_test.reshape((10000, 28, 28, 1))

    model = k.Sequential([
                     k.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
                     k.layers.MaxPool2D((2, 2)),
                     k.layers.Flatten(),
                     k.layers.Dense(64, activation=tf.nn.relu),
                     k.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
    model.fit(x_train, y_train, epochs=3)
    model.save('model.hdf5')


def processing():
    model = k.models.load_model('model.hdf5')
    img = load_img('3.png') #Изображение 28 на 28
    return give_answer(img, model)
    


def give_answer(img,model):
    

    img_array = img_to_array(img) #переводим картинку в массив
    img_array = img_array[:,:,0] #Берем один из цветовых каналов

    img_array = img_array.reshape(1,28,28,1) #меняем размерность массива
    img_array = img_array.astype('float32')/255 #приводим к диапазону чисел от 0 до 1

    img_array = abs(img_array - 1) #0-белое, 1-черное

    result = model.predict(img_array)

    return str(np.argmax(result)) #Возвращает ответ нейросети
