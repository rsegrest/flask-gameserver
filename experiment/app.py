from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context
# from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
#     close_room, rooms, disconnect
# from flask.ext.cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from flask_cors import CORS


#you may not need all these options
# from flask import Flask, render_template, request
# from flask.ext.socketio import SocketIO, emit, join_room, leave_room
# from flask.ext.cors import CORS



app = Flask(__name__, template_folder='./', static_folder='./', static_url_path='')
app.config['SECRET_KEY'] = 'some-super-secret-key'
app.config['DEFAULT_PARSERS'] = [
    'flask.ext.api.parsers.JSONParser',
    'flask.ext.api.parsers.URLEncodedParser',
    'flask.ext.api.parsers.FormParser',
    'flask.ext.api.parsers.MultiPartParser'
]
cors = CORS(app,resources={r"/*":{"origins":"*"}})
# socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins='*')

socketio.run(app,port=5000,host='0.0.0.0')




# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

# app = Flask(__name__)
# CORS(app)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()


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

# todo -- move board to separate class
board = [[0,0,0],[0,0,0],[0,0,0]]
playerX = None
playerO = None

# @app.route('/place')

# @app.route('/getboard')
# def getboard():
#     # return render_template('testboard.html', async_mode=socketio.async_mode)
#     return board

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
    print('JOINED ROOM')
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})
    emit('update_msg',
         {'msg': 'In rooms: ' + ', '.join(rooms()),
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

currentTurn = 'X'
def changeTurn():
    global currentTurn
    if currentTurn == 'X':
        currentTurn = 'O'
    else:
        currentTurn = 'X'

@socketio.on('join_room')
def on_join_room(message):
    print('joining room')
    join_room(message['room'])

@socketio.on('move')
def move(message):
    # print("*****MOVE*****")
    # board = [[0,0,0],[0,0,0],[0,0,0]]
    spacenum = message['move']
    row = spacenum // 3
    col = spacenum % 3
    board[row][col] = 1
    emit('board_update', {'board': board}, broadcast=True)
    changeTurn()
    emit('change_turn', {'turn': currentTurn}, broadcast=True)
    # print(message)

@socketio.event
def my_room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         to=message['room'])


@socketio.event
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})

@socketio.on('ping')
def test_ping():
    emit('pong', {'data': 'test'})

@socketio.on('set_name')
def set_username(message):
    print('****set_name')
    print(message)
    name = message['name']
    if (playerX == None):
        playerX = name
        emit('set_player', {'side': 'X'})
    elif (playerO == None):
        playerO = name
        emit('set_player', {'side': 'O'})
    emit('update_msg', {'msg': 'Welcome, '+name})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app)
