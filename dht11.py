from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(28))

while True:
    sleep(0.5)
    sensor.measure()
    print("Temperature: ", sensor.temperature(), " °C")
    print("Humidity: ", sensor.humidity(), " %")
    print("")
    sleep(0.5)