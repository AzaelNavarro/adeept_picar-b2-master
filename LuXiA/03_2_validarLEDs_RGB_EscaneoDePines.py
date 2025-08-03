from gpiozero import LED
from time import sleep

# Lista de posibles GPIO (BCM) en Raspberry Pi
# Excluye pines reservados: 0, 1 (I2C), 14, 15 (UART), etc.
test_pins = [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27]

print("Escaneando GPIOs para detectar conexiones con RGB1...")
for pin in test_pins:
    try:
        print(f"Probando GPIO {pin}...")
        led = LED(pin)
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.1)
    except Exception as e:
        print(f"GPIO {pin} falló: {e}")
