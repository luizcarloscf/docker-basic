import socket
import json
import numpy as np
import sys
import time
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s][%(asctime)s] %(message)s')

def parse_cli(args):
    return { "args": dict([arg.split('=', maxsplit=1) for arg in args[1:] ])}


HOST = 'forward-det' 
PORT = 5001

op = parse_cli(sys.argv[:])

m = int(op['args']['m'])
n = int(op['args']['n'])
f = float(op['args']['f'])
PORT = int (op['args']['port'])

print (op)

for i in range(0, m):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logging.info('Sending matrix to '+ str(HOST) + ' on port:' + str(PORT))
        s.connect((HOST, PORT))
        data = dict()
        data['matrix'] = np.random.random_sample((n,n)).tolist()
        data['initial-time'] = time.time()
        b = json.dumps(data).encode('utf-8')
        s.sendall(b)
    time.sleep(1/f)

