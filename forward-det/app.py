from flask import Flask, jsonify, request
import requests
import numpy as np
import time
import json


def make_status(ok):
    return {"status": ok}

class Service (object):

    def __init__(self):
        self.server = Flask (__name__)
        self.server.add_url_rule('/api/v1/determinante', 'determinante', self.matrix, methods=['POST', 'GET'])
    def matrix(self):
        if request.method == 'POST':
            content = request.get_data()
            content = json.loads(content)
            m = requests.post (url='http://0.0.0.0:5002/api/v1/result', json={'det': np.linalg.det(content['matrix'])})
            return jsonify(make_status(True)) 

app = Service()
app.server.run(debug=True, host='0.0.0.0', port=5001)
