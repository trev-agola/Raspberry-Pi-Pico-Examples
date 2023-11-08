from machine import Pin
from time import sleep

pir = Pin(0, Pin.IN, Pin.PULL_UP)
#Remember to adjust the sensitivity of PIR for better readings
led = Pin("LED", Pin.OUT)

while True:
    #Give time for the sensor to settle
    sleep(0.1)
    motion = pir.value()
    print("PIR Value: ", motion)
    if motion == 1:
        led.on()
        print("Motion detected!\n")
        sleep(1)
    else:
        led.off()
