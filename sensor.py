import random
import time

# Datos del sensor a simular
Basura_nueva_promedio = 20*0.5/3600
tiempo_sensado = 0.5


# Simulador 
#Agregar argumento para reiniciar con alguna señal desde cayenne
def Nivel():
    Basura_acumulada = 0
    while (1>0):
        # Random arroja un valor de cero a uno        
        Basura_nueva = random.random()*Basura_nueva_promedio
        Basura_acumulada = Basura_acumulada + Basura_nueva
        print(Basura_acumulada)
        time.sleep(0.5)

altura_tacho=1.5*100
Basura_acumulada = Nivel()
#While

#if(Basura_acumulada==0.8*altura_tacho):
    #while
    #mensaje    
    #cuado se vacíe BREAK (sale del bucle)
    #valor aleatorio que represente el tiempo en el que se vació el tacho,mnadar a cayene

    
