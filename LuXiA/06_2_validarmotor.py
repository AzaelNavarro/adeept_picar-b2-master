from gpiozero import Motor
from time import sleep

forward_pin = 17
backward_pin = 27  # O el que hayas puesto y funcione para atrás

motor = Motor(forward=forward_pin, backward=backward_pin)

print(f"Probando pin {forward_pin} para adelante")
motor.forward(speed=0.3)
sleep(3)
motor.stop()
sleep(1)

print(f"Probando pin {backward_pin} para atrás")
motor.backward(speed=0.3)
sleep(3)
motor.stop()
