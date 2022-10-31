from threading import Lock
from flask import Flask, session, request
# , render_template, session, request, copy_current_request_context
from flask import request
from flask_socketio import Namespace, emit, SocketIO, join_room, leave_room, close_room, rooms, disconnect

from constants.spacestates import EMPTY, B, R
from controller.c4_controller import C4Controller

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
async_mode = None
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/connectfour')
        
class ConnectFourNamespace(Namespace):

    def __init__(self, namespace):
        super().__init__(namespace)
        self.connect4Game = C4Controller()
        print('TicTacToeNamespace init')

    def on_my_ping(message, my_arg=None):
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('C4: received "my ping": ' + str(message))
        emit('my_pong', {'data': 'got it!'})

    def on_my_event(message):
        # print('TTT: received "my event": ' + str(message))
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
            {'data': message['data'], 'count': session['receive_count']})

    def on_my_broadcast_event(message):
        # print('TTT: received "my broadcast event": ' + str(message))
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


    def on_my_new_argument(self, my_arg=None):
        print('my_new_argument')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('new argument')
        emit('my_pong', {'id': request.sid})

    def on_connect(self, my_arg=None):
        # print('TTT: received "connect"') # + str(message))
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        global thread
        with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(background_thread)
        emit('my_response', {'data': 'Connected', 'count': 0})

    def on_disconnect(self, my_arg=None):
        # print('TTT: received "disconnect"')
        print('test_disconnect')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('* Client disconnected', request.sid)


    # TODO: verify "register_player" in controller
    def on_player_username(self, message):
        print('player_username')
        print('message', message)
        # if(my_arg is not None) and (my_arg != ''): print(my_arg)
        thisUserName = message['name']
        returnVal = self.connect4Game.register_player(thisUserName, request.sid, emit)
        return returnVal

    # TODO: verify try_move in controller
    def on_player_move(self, message):
        print('player_move')
        print('message', message)
        # if(my_arg is not None) and (my_arg != '') : print(my_arg)
        side = message['side']
        print('id:')
        print(request.sid)
        player_id = request.sid
        column = message['column']
        did_move = self.connect4Game.try_move(side, player_id, column, emit)
        if did_move:
            emit('update_board', { 'board': self.connect4Game.model.board }, broadcast=True)
            emit('update_game_status', {
                'status': self.connect4Game.model.game_status
            }, broadcast=True)
    # STUB
    def on_player_exit_room(self, my_arg=None):
        print('player_exit_room')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_exit_room', my_arg)

    # STUB
    def on_player_restart(self, my_arg=None):
        print('player_restart')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_restart', my_arg)

    # STUB: TODO
    def on_player_room_chat(self, my_arg=None):
        print('player_room_chat')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_room_chat', my_arg) # broadcast=True)

    def on_get_board_state(self, my_arg=None):
        print('C4: get_board_state')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_get_board_state', my_arg)

    # TODO: Verify "start_game_func" in controller
    # not needed?
    def on_start_game(self, my_arg=None):
        print('C4: start_game')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        self.connect4Game.start_game_func()

socketio.on_namespace(ConnectFourNamespace('/connectfour'))
if __name__ == '__main__':
    socketio.run(app)