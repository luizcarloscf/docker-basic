import socket
import json
import sys
class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        

    def connect(self):
        print ('Listening on...')
        self.server.listen()
        conn, addr = self.server.accept()
        return (conn, addr)

    def receive_package(self, conn, addr):
        print('Connected by', addr)
        b = b''
        while 1:
            tmp = conn.recv(1024)
            if tmp == b'':
                break
            b += tmp
        data = json.loads(b.decode('utf-8'))
        conn.close()
        return data
    def send_package(self, host, port, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            b = json.dumps(data).encode('utf-8')
            s.sendall(b)
            s.close()
        pass

server = Server(host='127.0.0.1', port=5001)

while 1:
    args = server.connect()
    package = server.receive_package(args[0], args[1])
    print (sys.getsizeof(package))
    server.send_package(host='127.0.0.1', port=5003, data=package)
