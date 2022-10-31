from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

from constants.spacestates import EMPTY, X, O


# import flask_cors # ?NEEDED?
from controller.tictactoe_controller import TicTacToeController
# from model.tictactoe_model import TicTacToeModel

# from engineio.payload import Payload

# Do we need this? avert an error seen before
# Payload.max_decode_packets = 50 / 500

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, async_mode=async_mode)
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()
tictactoeGame = TicTacToeController()

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.event
def my_broadcast_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.event
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.event
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('close_room')
def on_close_room(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         to=message['room'])
    close_room(message['room'])


@socketio.event
def my_room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         to=message['room'])


@socketio.event
def disconnect_request(my_arg=None):
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

# TESTED WITH POSTMAN, returns 'my_pong'
@socketio.event
def my_ping(my_arg=None):
    # print('my_ping')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    emit('my_pong')

# TESTED WITH POSTMAN, returns 'my_pong'
@socketio.event
def my_new_argument(my_arg=None):
    print('my_new_argument')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    print('new argument')
    emit('my_pong', {'id': request.sid})
    

# CLIENT MESSAGES:
#  - † PLAYER_USERNAME: Client sends name
#  - † PLAYER_MOVE: Player sends move
#  - † PLAYER_EXIT_GAME: Client exits game
#  - † PLAYER_RESTART: Client restarts game
#  - † PLAYER_EXIT_ROOM: Client exits room
#  - † PLAYER_ROOM_CHAT_MESSAGE: Client joins room

@socketio.event
def player_username(message):
    print('player_username')
    # print('message', message)
    thisUserName = message['name']
    returnVal = tictactoeGame.register_player(thisUserName)
    return returnVal

@socketio.event
def player_move(message):
    print('player_move')
    print('message', message)
    side = message['side']
    player_id = request.sid
    spacenum = message['spacenum']
    tictactoeGame.try_move(side, player_id, spacenum, emit)
    # emit('update_board', { 'board': tictactoeGame.model.board }, broadcast=True)
    # emit('update_game_status', {'status': tictactoeGame.model.game_status }, broadcast=True)

@socketio.event
def player_exit_game(my_arg=None):
    print('player_exit_game')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    emit('ack_player_exit_game', my_arg)

@socketio.event
def player_exit_room(my_arg=None):
    print('player_exit_room')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    emit('ack_player_exit_room', my_arg)

@socketio.event
def player_restart(my_arg=None):
    print('player_restart')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    emit('ack_player_restart', my_arg)

@socketio.event
def player_room_chat(my_arg=None):
    print('player_room_chat')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    emit('ack_player_room_chat', my_arg)

# TODO: Needs to return board state
@socketio.event
def get_board_state(my_arg=None):
    print('get_board_state')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    emit('ack_get_board_state', my_arg)

@socketio.event
def start_game(my_arg=None):
    print('start_game')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    tictactoeGame.start_game_func()

@socketio.event
def connect(my_arg=None):
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect')
def test_disconnect(my_arg=None):
    print('test_disconnect')
    if(my_arg is not None) and (my_arg != '') : print(my_arg)
    print('* Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app)
