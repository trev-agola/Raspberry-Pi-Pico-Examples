import network
import socket
from time import sleep
import machine
from machine import Pin
from umqtt.simple import MQTTClient
import random

led= Pin("LED", Pin.OUT)

def ledAction(message):
    ledBit = int(message.decode())
    if (ledBit==1):
        led.value(1)
    else:
        led.value(0)


import wificonnect
print("Connected to Wifi.")

mqtt_server = 'broker.hivemq.com'
mqtt_port = 1883 # non-SSL port
mqtt_topic = 'led_command' # Under "Feed info"
mqtt_client_id = 'pico' #must have a unique ID - good enough for now


def mqtt_connect():
    client = MQTTClient(client_id=mqtt_client_id, server=mqtt_server, port=mqtt_port, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    sleep(5)
    reset()


def callback(topic, msg):
    print("Received message: Topic= {}, Message= {}".format(topic.decode(), msg.decode()))
    ledAction(msg)

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()

client.set_callback(callback)



client.subscribe(mqtt_topic)


while True:
    wlan = network.WLAN(network.STA_IF)
    
    if wlan.isconnected():
        client.wait_msg()
        sleep(1)
    else:
        reconnect()