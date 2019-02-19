import socket
import json
import numpy as np
import sys
import time


def parse_cli(args):
    return { "args": dict([arg.split('=', maxsplit=1) for arg in args[1:] ])}


HOST = '127.0.0.1' 
PORT = 5001

op = parse_cli(sys.argv[:])

m = int(op['args']['m'])
n = int(op['args']['n'])
f = float(op['args']['f'])

print (op)

for i in range(0, m):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = np.random.randint(10, size=(n,n)).tolist()
        b = json.dumps(data).encode('utf-8')
        s.sendall(b)
        print (sys.getsizeof(data))
    time.sleep(1/f)

