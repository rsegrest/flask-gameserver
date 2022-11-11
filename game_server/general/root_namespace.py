from threading import Lock
from general.background_thread import background_thread, async_mode, thread, thread_lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from general.model.user_model import UserModel as User

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
# async_mode = None
# thread = None
# thread_lock = Lock()

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")


# @app.route('/')
# def index():
#     return render_template('index.html', async_mode=socketio.async_mode)


class RootNamespace(Namespace):
    
    def __init__(self, namespace, si):
        super().__init__(namespace)
        self.socketio = si

    def on_my_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']})

    def on_my_broadcast_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']},
             broadcast=True)

    def on_join(self, message):
        join_room(message['room'])
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'In rooms: ' + ', '.join(rooms()),
              'count': session['receive_count']})

    def on_leave(self, message):
        leave_room(message['room'])
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'In rooms: ' + ', '.join(rooms()),
              'count': session['receive_count']})

    def on_close_room(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                             'count': session['receive_count']},
             room=message['room'])
        close_room(message['room'])

    def on_my_room_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']},
             room=message['room'])

    def on_disconnect_request(self):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()

    def on_my_ping(self):
        print('on my ping')
        emit('my_pong')

    def on_connect(self, *args):
        print('Connected', request.sid, args)
        global thread
        with thread_lock:
            if thread is None:
                thread = self.socketio.start_background_task(background_thread)
        self.socketio.emit('my_response', {'data': 'Connected', 'count': 0})

    def on_disconnect(self):
        print('Client disconnected', request.sid)

    def on_register_username(self, message):
        print('on_register_username', message)
        print('id : ', request.sid)
        username = message['name']
        uid = request.sid
        user = User(user_name=username, user_id=uid)
        print('user to string : ' + str(user))
        # Add to user list
        
        # username = message['username']
        # password = message['password']
        # emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
        #                      'count': session['receive_count']},
        #      room=message['room'])
        # print('register user', username, password)


# socketio.on_namespace(RootNamespace('/'))

# if __name__ == '__main__':
#     socketio.run(app)
