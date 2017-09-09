import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 3100

connection = None

def connect():
    global connection
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((SERVER_IP, SERVER_PORT))

def putMessage(msg):
    msgLen = len(msg)
    msgLen_byteform = []
    for _ in range(4):
        msgLen_byteform.append(msgLen & 2**8-1)
        msgLen >>= 8
    msgLen_byteform.reverse()
    msgLen_byteform = bytes(msgLen_byteform)
    # print(msgLen_byteform + msg.encode(encoding = 'utf-8'))
    connection.send(msgLen_byteform + msg.encode(encoding = 'utf-8'))
    
def getMessage():
    msg = connection.recv(22*1024)
    msg = msg[4:].decode(encoding='utf-8')
    return msg
