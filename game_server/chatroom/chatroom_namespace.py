from threading import Lock
from flask import Flask, copy_current_request_context, session, request
# , render_template, session,
from flask_socketio import Namespace, join_room, leave_room, emit, SocketIO, disconnect, close_room, rooms

# from tictactoe.constants.spacestates import EMPTY, X, O
# from tictactoe.controller.tictactoe_controller import TicTacToeController

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# async_mode = None
# socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()
# socketio = None


def background_thread(self):
    count = 0
    while True:
        self.socketio.sleep(10)
        count += 1
        self.socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/chatroom')

class ChatroomNamespace(Namespace):
    # ...Game = ...Controller()

    def __init__(self, namespace, socketio):
        super().__init__(namespace)
        socketio = socketio
        # self....Game = ...Controller()
        print('Chatroom namespace init')


    def on_my_ping(message, my_arg=None):
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('Chatroom: received "my ping": ' + str(message))
        emit('my_pong', {'data': 'got it!'})

    def on_my_event(message):
        print('Chatroom: received "my event": ' + str(message))
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
            {'data': message['data'], 'count': session['receive_count']})

    def on_my_broadcast_event(message):
        print('Chatroom: received "my broadcast event": ' + str(message))
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

    def on_close_room(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                            'count': session['receive_count']},
            to=message['room'])
        close_room(message['room'])

    def on_my_room_event(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
            {'data': message['data'], 'count': session['receive_count']},
            to=message['room'])

    def on_disconnect_request(self):
        print('disconnect_request')
        @copy_current_request_context
        def can_disconnect(my_arg):
            print('can_disconnect')
            disconnect(my_arg=None)

        session['receive_count'] = session.get('receive_count', 0) + 1
        # for this emit we use a callback function
        # when the callback function is invoked we know that the message has been
        # received and it is safe to disconnect
        emit('my_response',
            {'data': 'Disconnected!', 'count': session['receive_count']},
            callback=can_disconnect)

    def on_connect(self, my_arg=None):
        print('Chatroom: received "connect"') # + str(message))
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        global thread
        with thread_lock:
            if thread is None:
                thread = self.socketio.start_background_task(background_thread(self))
        emit('my_response', {'data': 'Connected', 'count': 0})
            
    def on_disconnect(self, my_arg=None):
        print('Chatroom: received "disconnect"')
        print('test_disconnect')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('* Client disconnected', request.sid)
    
    # def on_my_new_argument(self, my_arg=None):
    #     print('my_new_argument')
    #     if(my_arg is not None) and (my_arg != '') : print(my_arg)
    #     print('new argument')
    #     emit('my_pong', {'id': request.sid})

    # def on_player_username(self, message):
    #     print('player_username')
    #     print('message', message)
    #     # if(my_arg is not None) and (my_arg != ''): print(my_arg)
    #     thisUserName = message['name']
    #     returnVal = self.tictactoeGame.register_player(thisUserName)
    #     return returnVal

    # STUB
    def on_player_exit_room(self, my_arg=None):
        print('player_exit_room')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_exit_room', my_arg)

    # STUB: TODO
    def on_player_room_chat(self, my_arg=None):
        print('player_room_chat')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_room_chat', my_arg) # broadcast=True)

# socketio.on_namespace(TicTacToeNamespace('/tictactoe'))
# if __name__ == '__main__':
#     socketio.run(app)