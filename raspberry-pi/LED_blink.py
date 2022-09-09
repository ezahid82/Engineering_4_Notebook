# type: ignore
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:

    led.value = True
    time.sleep(0.50)
    led.value = False
    time.sleep(0.50)