from machine import Pin
from time import sleep

led=Pin(0, Pin.OUT)
while True:
    led.toggle()
    sleep(1)