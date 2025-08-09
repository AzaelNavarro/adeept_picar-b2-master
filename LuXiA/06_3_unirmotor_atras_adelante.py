from gpiozero import Motor
from time import sleep

def test_motor_pins(forward_pin, backward_pin, duration=3):
    motor = Motor(forward=forward_pin, backward=backward_pin)
    print(f"Probando motor con forward={forward_pin} y backward={backward_pin}")

    motor.forward(speed=0.3)
    print("Adelante")
    sleep(duration)

    motor.backward(speed=0.3)
    print("Atrás")
    sleep(duration)

    motor.stop()
    print("Detenido\n")
    sleep(1)

if __name__ == "__main__":
    # Primer conjunto de pines
    test_motor_pins(17, 27, 3)

    # Segundo conjunto de pines
    test_motor_pins(17, 18, 3)
