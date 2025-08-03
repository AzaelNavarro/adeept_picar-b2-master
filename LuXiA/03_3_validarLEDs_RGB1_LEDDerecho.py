#!/usr/bin/env python3
import time
from gpiozero import LED

# Canales RGB del LED (RGB1 - lado derecho)
led_red = LED(22)
led_green = LED(23)
led_blue = LED(24)

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
