from network import processing

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    processing()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)