from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import json
data={'temp':'32', 'humid': '23', 'soil':'156', 'light' : '10'}
app = Flask(__name__)
CORS(app)
@app.route('/get/' , methods = ['GET'])
def get():
    with open("data.json", 'r') as file:
        return jsonify(json.loads(file.read()))


@app.route('/post/' , methods = ['GET','POST'])
def post():
    content = request.get_json()
    data = dict()
    data['temp'] = content.get('Temperature')
    data['humidity'] = content.get('Humidity')
    data['mousture'] = content.get('Soil Moisture')
    data['light'] = content.get('Light Intensity')
    with open("data.json", 'w') as file:
      file.write(json.dumps(data))
    return jsonify('success')

if __name__ == "__main__":
    app.run('192.168.12.84')
