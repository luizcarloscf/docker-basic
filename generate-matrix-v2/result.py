import socket
import json
import sys
import time

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
        data['final-time'] = time.time()
        conn.close()
        return data
    

server = Server(host='127.0.0.1', port=5003)
package = dict()

while 1:
    args = server.connect()
    package = server.receive_package(args[0], args[1])
    print ('-------------Received matrix------------')
    if 'det' in package:
        print ('Determinant: ' + str(package['det']))
        print ('Time interval: ' + str(package['final-time']-package['initial-time']))



