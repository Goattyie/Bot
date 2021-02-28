import random
import requests

token = '7551bf2d20f5008eb5525ab0d35ee42e7b4e409aa9cc9a1098052faeca0e1d5d200eaed5dedb3e2528a6c'
v = 5.103


def send_message(id_type, id, message):
    requests.get('https://api.vk.com/method/messages.send',
    params={'access_token': token, 'v': v, 'random_id': random.randint(0, 999999999), id_type: id, 'message': message})