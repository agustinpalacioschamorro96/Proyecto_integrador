#!/usr/bin/env python
import cayenne.client
import time
import logging
import random
import time

# Datos del sensor a simular
basura_cm = 20
media_basura = basura_cm*0.5/3600
maximo_tacho = 0.1

# Datos Temporales
minutos_max = 0.1
tiempo_max_seg = minutos_max*60 

# Funciones del simulador

def Generar_basura(basura_total):
    basura_nueva = random.random()*media_basura
    basura_total = basura_nueva + basura_total
    return basura_total


def Tiempo_vaciado():
    tiempo = random.random()*tiempo_max_seg
    time.sleep(tiempo)
    return tiempo

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "a3fc4dc0-ced1-11eb-8779-7d56e82df461"
MQTT_PASSWORD  = "8006e15e4a1c2d2cc5a023c56fb76d62564ff5c0"
MQTT_CLIENT_ID = "e6dc95c0-d83e-11eb-883c-638d8ce4c23d"


client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)


## Programita que simula el llenado y aviso de los tiempos ##

basura_total = 0 
error = 0.2
tiempo_enviar_estado = 1  #Tiempo determinado a enviar a cayenne
tiempo_sensado = 0.5 
tiempo_total = 0

while True:
    client.loop()
    
    basura_total = Generar_basura(basura_total)
    
    if(basura_total > maximo_tacho*0.8 + error or basura_total == maximo_tacho*0.8 - error ):
        #loop
        # Tacho lleno
        #               Mandar mensaje de lleno
        #               Hay que contar tiempo de espera para recoger y avisar llenado
        Tiempo = Tiempo_vaciado()
        #               Aca mandariamos mensaje del tiempo
        print(Tiempo)
        basura_total = 0
    else :
        # Tacho no lleno
        #               Debemos enviar informacion de estado cada cierto tiempo y contar tiempo de llenado
        tiempo_total = tiempo_total + tiempo_sensado
        
        if (tiempo_total >= tiempo_enviar_estado):
            # Enviar informacion de estado de basura
            tiempo_enviar_estado = 0
            print(basura_total)
            client.virtualWrite(4, basura_total*100, dataType="nivel_basura", dataUnit="cm")

        time.sleep(tiempo_sensado)
   