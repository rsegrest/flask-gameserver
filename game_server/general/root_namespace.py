import sys
from threading import Lock

# from general.background_thread import background_thread, async_mode, thread, thread_lock
from flask import Flask, render_template, request, session
from flask_socketio import (Namespace, SocketIO, close_room, disconnect, emit,
                            join_room, leave_room, rooms)

sys.path.append('..')
<<<<<<< HEAD
from threading import Lock

# from model.user_model import UserModel as User
from chatroom.model.message_list_model import MessageListModel
from general.model.user_model import UserModel as User
=======
from general.model.user_model import UserModel as User
from chatroom.model.message_list_model import MessageListModel as MessageList
from general.model.game_session_model import GameSessionModel as GameSession
from general.model.server_session_model import ServerSessionModel as ServerSession

from threading import Lock
>>>>>>> 7b3dc5e23fedf7824db329c1f4de576b8c654017

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
# async_mode = None
# thread = None
# thread_lock = Lock()


# @app.route('/')
# def index():
#     return render_template('index.html', async_mode=socketio.async_mode)


global socketio
async_mode = None
thread = None
thread_lock = Lock()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*", logger=True, engineio_logger=True)


def background_thread(): # (socketio):
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/')

class RootNamespace(Namespace):
    
    def __init__(self, namespace, si=None):
        super().__init__(namespace)
        self.game_session = GameSession('THE_LOBBY', 'CHAT_ROOM')
        self.server_session = ServerSession()
        self.message_list = MessageList()

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
        print('on_disconnect_request')
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()
        print('disconnected')

    def on_my_ping(self):
        print('on my ping')
        emit('my_pong')

    def on_connect(self, *args):
        print('Connected', request.sid, args)
        global thread
        with thread_lock:
            if thread is None:
                print('Creating thread')
                # thread = self.socketio.start_background_task(background_thread(socketio=self.socketio))
                thread = socketio.start_background_task(background_thread)
        socketio.emit('my_response', {'data': 'Connected', 'count': 0})

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

    def on_request_users_in_room(self):
        print('on_request_users_in_room')
        self.socketio.emit('users', {'users': self.game_session.get_player_list()})
    
    def on_request_games_available(self):
        print('on_request_games_available')
        self.socketio.emit('games', {'games': self.server_session.get_game_types_list()})
    
    def on_request_messages(self):
        print('on_request_messages')
        message_list = self.message_list.get_message_list()
        print('message_list is currently : ', message_list)
        socketio.emit('messages', {'messages': message_list})
        
    def on_send_chat_message(self, message):
        print('on_send_chat_message')
        print('message is : ', message)
        self.message_list.add_message(
            username=message['user_name'],
            content=message['content']
        )
        socketio.emit('message_list_update', {'messages': self.message_list.get_message_list()})


socketio.on_namespace(RootNamespace('/'))

if __name__ == '__main__':
    socketio.run(app, debug=True)
