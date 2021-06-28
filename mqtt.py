#!/usr/bin/env python
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "a3fc4dc0-ced1-11eb-8779-7d56e82df461"
MQTT_PASSWORD  = "8006e15e4a1c2d2cc5a023c56fb76d62564ff5c0"
MQTT_CLIENT_ID = "e6dc95c0-d83e-11eb-883c-638d8ce4c23d"


client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)

i=0
timestamp = 0

while True:
    client.loop()
    
    if (time.time() > timestamp + 10):
        client.virtualWrite(2, 30, dataType="tiempo", dataUnit="Segundos")
        client.virtualWrite(1, 156)
        timestamp = time.time()
        i = i+1
