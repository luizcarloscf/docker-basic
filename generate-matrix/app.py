from flask import Flask, jsonify, request
import requests
import json
import numpy as np
import time



def make_status(ok):
    return {"status": ok}

class Service (object):
    def __init__(self):
        self.server = Flask (__name__)
        self.server.add_url_rule('/api/v1/matrix', 'matrix', self.matrix, methods=['POST'])
    def matrix(self):
        if request.method == 'POST':
            content = request.get_data(as_text=True)
            content = json.loads(content)
            m = int(content['m'])
            n = int(content['n'])
            f = int(content['f'])
            for i in range(0, m):
                m = requests.post (url='http://172.18.0.1:5001/api/v1/determinante', json={'matrix': np.random.randint(10, size=(n,n)).tolist()})
                time.sleep(f)
            return jsonify(make_status(True))
            
            
app = Service()
app.server.run(debug=True,host=172.18.0.1, port=5000)
