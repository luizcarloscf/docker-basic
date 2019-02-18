import socket
import json

HOST = '127.0.0.1' 
PORT = 5000

data = {'m': 2, 'n':2, 'f':2}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


b = json.dumps(data).encode('utf-8')
s.sendall(b)


s.close()