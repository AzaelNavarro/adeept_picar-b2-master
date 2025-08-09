from gpiozero import Motor
from time import sleep

# Intenta invertir los pines si no funciona hacia atrás
motor = Motor(forward=17, backward=18)  # cambiar los pines

motor.forward(speed=0.3)
print("Adelante")
sleep(5)

motor.backward()
print("Atrás")
sleep(5)

motor.stop()
print("Detenido")
