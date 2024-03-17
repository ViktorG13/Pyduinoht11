from ArduinoSensorDriver import ArduinoSensorDriver
from flask import Flask
app = Flask(__name__)

sensor = ArduinoSensorDriver()
sensor.connect()

@app.route("/v1/data")
def response_data():
  return f"{sensor.read_sensor()}"

if __name__ == "__main__":
  app.run(host="localhost", port=5500, debug=True)
