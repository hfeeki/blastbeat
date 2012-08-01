import zmq

context = zmq.Context()
# create the dealer socket
socket = context.socket(zmq.DEALER)
# authorize it setting the identity
socket.setsockopt(zmq.IDENTITY, 'sharedcanvas')
# connect to blastbeat
socket.connect('tcp://127.0.0.1:5000')

# start receiving messages
while True:
    sid, msg_type, msg_body = socket.recv_multipart()
    if msg_type == 'ping':
        socket.send(sid, zmq.SNDMORE)
        socket.send('pong', zmq.SNDMORE)
        socket.send('')
    elif msg_type == 'uwsgi':
        socket.send(sid, zmq.SNDMORE)
        socket.send('join', zmq.SNDMORE)
        socket.send('sharedcanvas')
    elif msg_type == 'websocket':
        socket.send(sid, zmq.SNDMORE)
        socket.send('sharedcanvas:websocket', zmq.SNDMORE)
        socket.send(msg_body)
