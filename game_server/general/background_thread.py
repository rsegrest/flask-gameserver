from threading import Lock

# global socketio
async_mode = None
thread = None
thread_lock = Lock()

def background_thread(socketio): # (socketio):
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/')
