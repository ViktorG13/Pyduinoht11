import json
import serial
from time import sleep

class ArduinoSensorDriver:
  def __init__(self, port="/dev/ttyACM0", baudrate=9600):
    self.port = port
    self.baudrate = baudrate
    self.arduino = None

  def connect(self):
    while True:
      try:
        self.arduino = serial.Serial(self.port, self.baudrate)
        print("Connected")
        break
      except serial.SerialException:
        pass
      sleep(1)

  def read_sensor(self):
    try:
      while True:
        data = self.arduino.readline().decode().strip()
        if 'T' in data and 'H' in data:
          temperature, humidity = data.split('T')[1].split('H')
          sensor = {"temperature": temperature, "humidity": humidity}
          return json.dumps(sensor)
        self.arduino.flush()
    except KeyboardInterrupt:
      self.arduino.close()
      print("Disconnected")

if __name__ == "__main__":
  sensor_driver = ArduinoSensorDriver()
  sensor_driver.connect()
  print(sensor_driver.read_sensor())
