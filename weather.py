#!/usr/bin/env python3

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Dummy data — replace with real sensor data later
    data = {
        "temperature": 22.5,
        "humidity": 55.0,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
