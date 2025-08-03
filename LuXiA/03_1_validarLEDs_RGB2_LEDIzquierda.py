#!/usr/bin/env python3
import time
#!/usr/bin/env python3
import time
from gpiozero import LED

# Canales RGB del LED (RGB2 confirmado)
led_red = LED(10)
led_green = LED(9)
led_blue = LED(25)

if __name__ == '__main__':
    while True:
        print("Rojo")
        led_red.on()
        led_green.off()
        led_blue.off()
        time.sleep(1)

        print("Verde")
        led_red.off()
        led_green.on()
        led_blue.off()
        time.sleep(1)

        print("Azul")
        led_red.off()
        led_green.off()
        led_blue.on()
        time.sleep(1)

        print("Blanco")
        led_red.on()
        led_green.on()
        led_blue.on()
        time.sleep(1)

        print("Apagado")
        led_red.off()
        led_green.off()
        led_blue.off()
        time.sleep(1)
