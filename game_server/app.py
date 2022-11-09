from general.root_namespace import RootNamespace
from chatroom.chatroom_namespace import ChatroomNamespace
from tictactoe.tictactoe_namespace import TicTacToeNamespace
from yahtzee.yahtzee_namespace import YahtzeeNamespace
# from connectfour.connectfour_namespace import ConnectFourNamespace

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# socketio = SocketIO(app, async_mode=async_mode)
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
socketio.on_namespace(RootNamespace('/', socketio))
socketio.on_namespace(ChatroomNamespace('/chatroom', socketio))
socketio.on_namespace(TicTacToeNamespace('/tictactoe', socketio))
# socketio.on_namespace(ConnectFourNamespace('/connectfour', socketio))
# socketio.on_namespace(YahtzeeNamespace('/yahtzee', socketio))
socketio.run(app)