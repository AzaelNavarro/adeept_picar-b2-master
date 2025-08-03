from gpiozero import LED
import time

led = LED(27) 

#RGB2 (Izquierda): 9 (verde), 25 (azul) y el 10 (rojo) funcionan apuntando al RGB2
#RGB1 (Derecha): 22 (rojo), 23 (verde), 24 (azul),  
#

while True:
    led.on()
    print("LED encendido")
    time.sleep(1)
    led.off()
    print("LED apagado")
    time.sleep(1)
