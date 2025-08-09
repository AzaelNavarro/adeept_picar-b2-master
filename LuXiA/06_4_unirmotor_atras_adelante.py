from gpiozero import Motor
from time import sleep

def test_motor(forward_pin, backward_pin, duration=3):
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

if __name__ == "__main__":
    # Usar el set de pines que sabes que funciona
    test_motor(17, 27)
    # Si quieres probar otro set:
    test_motor(17, 18)
