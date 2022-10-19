from threading import Lock
from flask import Flask
# , render_template, session, request, copy_current_request_context
from flask import request
from flask_socketio import Namespace, emit, SocketIO
# emit, join_room, leave_room, close_room, rooms, disconnect

from constants.spacestates import EMPTY, X, O
from controller.tictactoe_controller import TicTacToeController

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
async_mode = None
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()

class TicTacToeNamespace(Namespace):
    tictactoeGame = TicTacToeController()

    # def __init__(self, namespace):
    #     super().__init__(namespace)
    #     print('TicTacToeNamespace init')

    def on_my_ping(message, my_arg=None):
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('TTT: received "my ping": ' + str(message))
        emit('my_pong', {'data': 'got it!'})

    def on_my_event(message):
        print('TTT: received "my event": ' + str(message))

    def on_my_broadcast_event(message):
        print('TTT: received "my broadcast event": ' + str(message))

    def on_connect(self):
        print('TTT: received "connect"') # + str(message))

    def on_disconnect(self):
        print('TTT: received "disconnect"')
    
    def on_player_username(self, message):
        print('player_username')
        print('message', message)
        # if(my_arg is not None) and (my_arg != ''): print(my_arg)
        if (self.tictactoeGame.num_players_registered() < 2):
            print('assigning player')
            side_assigned = self.tictactoeGame.register_a_player(message['name'], request.sid)
            # TicTacToeModel.num_players_registered += 1
            # TicTacToeModel.player_username = my_arg
            # TicTacToeModel.player_id = request.sid
            # print('player_username: ' + my_arg)
            # emit('my_pong', {'id': request.sid})
            emit('ack_player_username', {
                'id': request.sid,
                'username': self.tictactoeGame.get_player_names(), # [request.sid]})
                'side': side_assigned, # [request.sid]
            })
            print('returning True')
            return True
        return False

    def on_player_move(self, message):
        print('player_move')
        print('message', message)
        # if(my_arg is not None) and (my_arg != '') : print(my_arg)
        side = message['side']
        print('id:')
        print(request.sid)
        player_id = request.sid
        spacenum = message['spacenum']
        self.tictactoeGame.try_move(side, player_id, spacenum)
        # emit('ack_player_move', message)
        emit('update_board', { 'board': self.tictactoeGame.model.board }, broadcast=True)
        emit('update_game_status', {'status': self.tictactoeGame.model.game_status }, broadcast=True)

    def on_player_exit_game(self, my_arg=None):
        print('player_exit_game')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_exit_game', my_arg)

    def on_player_exit_room(self, my_arg=None):
        print('player_exit_room')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_exit_room', my_arg)

    def on_player_restart(self, my_arg=None):
        print('player_restart')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_restart', my_arg)

    def on_player_room_chat(self, my_arg=None):
        print('player_room_chat')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_room_chat', my_arg)

    def on_get_board_state(self, my_arg=None):
        print('get_board_state')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_get_board_state', my_arg)

    # not needed?
    def on_start_game(self, my_arg=None):
        print('start_game')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        torf = False
        if self.tictactoeGame.num_players_registered() == 2:
            self.tictactoeGame.start_game()
            if self.tictactoeGame.has_game_started():
                torf = True
        print('torf', torf)
        emit('ack_start_game', {'starting_game': str(torf)})


socketio.on_namespace(TicTacToeNamespace('/tictactoe'))
if __name__ == '__main__':
    socketio.run(app)