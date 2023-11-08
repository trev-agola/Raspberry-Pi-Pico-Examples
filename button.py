from machine import Pin
from time import sleep

button = Pin(15, Pin.OUT, Pin.PULL_DOWN)

while True:
    #if button.value():
    if button.value() == 1:
        led.toggle()
        sleep(1)