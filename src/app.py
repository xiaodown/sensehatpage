from flask import Flask, render_template, jsonify
from sense_reader import get_sensor_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    temperature, humidity = get_sensor_data()
    return jsonify(temperature=temperature, humidity=humidity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)