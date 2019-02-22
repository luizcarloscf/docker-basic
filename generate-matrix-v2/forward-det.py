import socket
import json
import sys
import numpy as np


host = '0.0.0.0'
port_on = 5001
port_to = 5003

class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        print (f'Listening on: {self.host}:{self.port}')
        self.server.listen()

    def connect(self):
        conn, addr = self.server.accept()
        return (conn, addr)

    def receive_package(self, conn, addr):
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

def parse_cli(args):
    return { "args": dict([arg.split('=', maxsplit=1) for arg in args[1:] ])}

op = parse_cli(sys.argv[:])
port_on = int (op['args']['port_on'])
port_to = int (op['args']['port_to'])
server = Server(host=host, port=port_on)

while 1:
    args = server.connect()
    package = server.receive_package(args[0], args[1])
    package['det'] = np.linalg.det(np.linalg.inv(package['matrix']))
    print ('Received package and sending to ' + host + ':' + str(port_to))
    server.send_package(host='result', port=port_to, data=package)
