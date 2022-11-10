from threading import Lock
from flask import Flask, copy_current_request_context, session, request
# , render_template, session,
from flask_socketio import Namespace, join_room, leave_room, emit, SocketIO, disconnect, close_room, rooms
from general.background_thread import background_thread, async_mode, thread, thread_lock

from tictactoe.constants.spacestates import EMPTY, X, O
from tictactoe.controller.tictactoe_controller import TicTacToeController

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# async_mode = None
# socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()


def background_thread(self):
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        self.socketio.sleep(10)
        count += 1
        self.socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/tictactoe')

class TicTacToeNamespace(Namespace):
    # tictactoeGame = TicTacToeController()

    def __init__(self, namespace, socketio):
        super().__init__(namespace)
        self.socketio = socketio
        self.tictactoeGame = TicTacToeController()
        print('TicTacToeNamespace init')


    def on_my_ping(message, my_arg=None):
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('TTT: received "my ping": ' + str(message))
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
                thread = self.socketio.start_background_task(background_thread(self))
        emit('my_response', {'data': 'Connected', 'count': 0})
            
    def on_disconnect(self, my_arg=None):
        # print('TTT: received "disconnect"')
        print('test_disconnect')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        print('* Client disconnected', request.sid)
    
    def on_player_username(self, message):
        print('player_username')
        print('message', message)
        # if(my_arg is not None) and (my_arg != ''): print(my_arg)
        thisUserName = message['name']
        returnVal = self.tictactoeGame.register_player(thisUserName)
        return returnVal

        # if (self.tictactoeGame.num_players_registered() < 2):
        #     print('assigning player')
        #     side_assigned = self.tictactoeGame.register_a_player(message['name'], request.sid)
        #     emit('ack_player_username', {
        #         'id': request.sid,
        #         'username': self.tictactoeGame.get_player_names(), # [request.sid]})
        #         'side': side_assigned, # [request.sid]
        #     })
        #     print('returning True')
        #     return True
        # return False

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
        # emit('update_board', { 'board': self.tictactoeGame.model.board }, broadcast=True)
        # emit('update_game_status', {'status': self.tictactoeGame.model.game_status }, broadcast=True)

    # STUB
    def on_player_exit_game(self, my_arg=None):
        print('player_exit_game')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_player_exit_game', my_arg)

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
        print('get_board_state')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        emit('ack_get_board_state', my_arg)

    # not needed?
    def on_start_game(self, my_arg=None):
        print('start_game')
        if(my_arg is not None) and (my_arg != '') : print(my_arg)
        self.tictactoeGame.start_game_func()
        # torf = False
        # if self.tictactoeGame.num_players_registered() == 2:
        #     self.tictactoeGame.start_game()
        #     if self.tictactoeGame.has_game_started():
        #         torf = True
        # print('torf', torf)
        # emit('ack_start_game', {'starting_game': str(torf)})


# socketio.on_namespace(TicTacToeNamespace('/tictactoe'))
# if __name__ == '__main__':
#     socketio.run(app)