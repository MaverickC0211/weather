
#!/usr/bin/env python3

from flask import Flask, render_template
from sensors import dht22_reader  # assuming you have this file
import csv
from datetime import datetime

app = Flask(__name__)

DATA_LOG = "data/weather_log.csv"

# Helper function to log and retrieve data
def log_sensor_data():
    temperature, humidity = dht22_reader.read_sensor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(DATA_LOG, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temperature, humidity])
    
    return {
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity
    }

# Home route to show current data
@app.route('/')
def index():
    latest_data = log_sensor_data()
    return render_template('index.html', data=latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Accessible on local network
