from chatroom.chatroom_namespace import ChatroomNamespace
from flask import Flask, render_template, request, session
from flask_socketio import (Namespace, SocketIO, close_room, disconnect, emit,
                            join_room, leave_room, rooms)
from general.background_thread import (async_mode, background_thread, thread,
                                       thread_lock)
from general.root_namespace import RootNamespace
from tictactoe.tictactoe_namespace import TicTacToeNamespace
from yahtzee.yahtzee_namespace import YahtzeeNamespace

# from connectfour.connectfour_namespace import ConnectFourNamespace


# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


# socketio = SocketIO(app, async_mode=async_mode)
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*", logger=True, engineio_logger=True)
socketio.on_namespace(RootNamespace('/')) #, si=socketio))
# socketio.on_namespace(RootNamespace('/', socketio))
# socketio.on_namespace(ChatroomNamespace('/chatroom', socketio))
# socketio.on_namespace(TicTacToeNamespace('/tictactoe', socketio))
# socketio.on_namespace(ConnectFourNamespace('/connectfour', socketio))
# socketio.on_namespace(YahtzeeNamespace('/yahtzee', socketio))
socketio.run(app, debug=True)