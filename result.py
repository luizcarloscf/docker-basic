import socket
import json
import sys
import time
import logging

class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        logging.info('Listening on:' + str(self.host) + ":" + str(self.port)) 
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
    
def parse_cli(args):
    return { "args": dict([arg.split('=', maxsplit=1) for arg in args[1:] ])}

op = parse_cli(sys.argv[:])
port = int (op['args']['port'])

server = Server(host='0.0.0.0', port=port)
package = dict()

while 1:
    args = server.connect()
    package = server.receive_package(args[0], args[1])
    print ('-------------Received matrix------------')
    if 'det' in package:
        logging.info ('Determinant: ' + str(package['det']))
        logging.info (print ('Time interval: ' + str(package['final-time']-package['initial-time'])))



