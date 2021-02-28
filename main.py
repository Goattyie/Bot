from api import send_message
from network import machine_learning, predict

from tensorflow.python.keras.preprocessing.image import load_img
from tensorflow import keras as k
from flask import Flask, request
from api import send_message
from PIL import Image
import requests
app = Flask(__name__)


@app.route('/', methods=['POST'])
def work():
    json = request.json

    if json and json['type'] == 'confirmation' and json['group_id'] == 202916110:
            return 'ecffc532'

    if json and json['type'] == 'message_new':
        url = None

        try:
            if json['object']['message']['attachments'][0]['photo']['sizes'][-1]['url']:
                url = json['object']['message']['attachments'][0]['photo']['sizes'][-1]['url']
        except: pass
        try:
            if json['object']['message']['attachments'][0]['graffiti']['url']:
                url = json['object']['message']['attachments'][0]['graffiti']['url']
        except: pass

        if url:
            image = requests.get(url)

            with open('image.png', 'wb') as file:
                file.write(image.content)
            
            image = Image.open('image.png').resize((28, 28), Image.ANTIALIAS)
            image.save('image.png')
            image = load_img('image.png')

            try:
                send_message('peer_id', json['object']['message']['from_id'], predict(image))
            except:
               print('error')

    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)