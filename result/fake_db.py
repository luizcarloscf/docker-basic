from flask import jsonify
def make_status(ok):
    return {"status": ok}

class FakeDB(object):
    # constructor
    def __init__(self):
        self.dets = []
        self.counter = 0
      
    def addDet(self, det):
        det['ID'] = self.counter
        self.dets.append(det)
        self.counter = self.counter + 1
        return jsonify(make_status(True))