from machine import Pin
from time import sleep
led_onboard = Pin("LED", Pin.OUT)

while True:
    led_onboard.value(1)
    sleep(1)
    led_onboard.value(0)
    sleep(1)