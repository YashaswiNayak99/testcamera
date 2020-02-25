import eventlet
import socketio
from flask import Flask
from flask_cors import CORS

flaskapp = Flask(__name__)
CORS(flaskapp)

sio = socketio.Server(cors_allowed_origins='*')
app = app = socketio.WSGIApp(sio, flaskapp)


@flaskapp.route("/")
def helloWorld():
    return "Hello, cross-origin-world!"


@sio.event
def connect(sid, environ):
    print('CONN:')
    print('connect', sid)


@sio.on('message')
def my_message(sid, data):
    print('MESSAGE:')
    print('message', data)


@sio.on('stream')
def my_stream(sid, data):
    print('STREAM:')
    print('stream', data)


@sio.event
def disconnect(sid):
    print('disconnect', sid)


if __name__ == '__main__':
    print('Hello')
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
