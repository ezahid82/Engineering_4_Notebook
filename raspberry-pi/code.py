# as of 09.02.22 we are working on how to use
# [VS Code] [Python 10.6] and using [Github]
# to easily code better and efficiently.
# - Ezhar Zahid


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