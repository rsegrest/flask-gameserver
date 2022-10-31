from threading import Lock
from flask import Flask
# , render_template, session, request, copy_current_request_context
from flask import request
from flask_socketio import Namespace, emit, SocketIO
# emit, join_room, leave_room, close_room, rooms, disconnect

from constants.spacestates import EMPTY, X, O
from controller.c4_controller import Connect4Controller

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
async_mode = None
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()

class ConnectFourNamespace(Namespace):
    connect4Game = Connect4Controller()

    # def __init__(self, namespace):
    #     super().__init__(namespace)
    #     print('TicTacToeNamespace init')

    def on_my_ping(message, my_arg=None):
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('C4: received "my ping": ' + str(message))
        emit('my_pong', {'data': 'got it!'})

    def on_my_event(message):
        print('C4: received "my event": ' + str(message))

    def on_my_broadcast_event(message):
        print('C4: received "my broadcast event": ' + str(message))

    def on_connect(self):
        print('C4: received "connect"') # + str(message))

    def on_disconnect(self):
        print('C4: received "disconnect"')
    
    def on_player_username(self, message):
        print('C4: player_username')
        print('message', message)
        # if(my_arg is not None) and (my_arg != ''): print(my_arg)
        if (self.connect4Game.num_players_registered() < 2):
            print('assigning player')
            side_assigned = self.connect4Game.register_a_player(
                message['name'], request.sid
            )
            # TicTacToeModel.num_players_registered += 1
            # TicTacToeModel.player_username = my_arg
            # TicTacToeModel.player_id = request.sid
            # print('player_username: ' + my_arg)
            # emit('my_pong', {'id': request.sid})
            emit('ack_player_username', {
                'id': request.sid,
                'username': self.connect4Game.get_player_names(), # [request.sid]})
                'side': side_assigned, # [request.sid]
            })
            print('returning True')
            return True
        return False

    def on_player_move(self, message):
        print('C4: player_move')
        print('message', message)
        # if(my_arg is not None) and (my_arg != '') : print(my_arg)
        column = message['column']
        print('id:')
        print(request.sid)
        player_id = request.sid
        column = message['column']
        self.connect4Game.try_move(self, player_id, column)
        # emit('ack_player_move', message)
        emit('update_board', { 'board': self.connect4Game.model.board }, broadcast=True)
        emit('update_game_status', {'status': self.connect4Game.model.game_status }, broadcast=True)

    def on_player_exit_game(self, my_arg=None):
        print('C4: player_exit_game')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_exit_game', my_arg)

    def on_player_exit_room(self, my_arg=None):
        print('C4: player_exit_room')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_exit_room', my_arg)

    def on_player_restart(self, my_arg=None):
        print('C4: player_restart')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_restart', my_arg)

    def on_player_room_chat(self, my_arg=None):
        print('C4: player_room_chat')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_room_chat', my_arg)

    def on_get_board_state(self, my_arg=None):
        print('C4: get_board_state')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_get_board_state', my_arg)

    # not needed?
    def on_start_game(self, my_arg=None):
        print('C4: start_game')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        torf = False
        if self.connect4Game.num_players_registered() == 2:
            self.connect4Game.start_game()
            if self.connect4Game.has_game_started():
                torf = True
        print('torf', torf)
        emit('ack_start_game', {'starting_game': str(torf)})


socketio.on_namespace(ConnectFourNamespace('/connectfour'))
if __name__ == '__main__':
    socketio.run(app)