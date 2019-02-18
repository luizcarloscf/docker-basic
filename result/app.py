from flask import Flask, jsonify, request
from fake_db import FakeDB
import requests
import numpy as np
import time
import json


def make_status(ok):
    return {"status": ok}

class Service (object):

    def __init__(self):
        self.db = FakeDB()
        self.server = Flask (__name__)
        self.server.add_url_rule('/api/v1/result', 'result', self.matrix, methods=['POST', 'GET'])
    def matrix(self):
        if request.method == 'POST':
            content = request.get_data()
            content = json.loads(content)
            self.db.addDet(content)
            return jsonify(make_status(True))
        elif request.method == 'GET':
            return jsonify (self.db.dets)
            

            
            


app = Service()
app.server.run(debug=True, host='172.17.0.1', port=5002)
