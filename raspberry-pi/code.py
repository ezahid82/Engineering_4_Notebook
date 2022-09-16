# type: ignore

import time
import board
import digitalio



led = digitalio.DigitalInOut(board.GP15)     # Green LED.
led2 = digitalio.DigitalInOut(board.GP16)    # Red LED.
led.direction = digitalio.Direction.OUTPUT      # Makes it so the Green LED's PIN direction is going OUT.
led2.direction = digitalio.Direction.OUTPUT     # Makes it so the Red LED's PIN direction is going OUT.



for x in range(10, -1, -1):      #  Using a [for] loop to express the values between 0-10 and making it count down by [-1].
   # time.sleep(0.5)           # Adds a delay in between the countdown.
    print(x)                # Prints all the values going from [10] down to [0] by the increment amount (-1).
    time.sleep(0.5)

    
    if (x <= 10 and x >= 1):        # Adds a range to which the Green LED with be [True].
        led.value = True            # Keeps the Green LED on.
        time.sleep(0.5)             # Adds a time limit to how long it will stay on.
        led.value = False           # Turns the Green LED off.
    else:
        led2.value = True           # Turns the Red LED on.
        print("liftoff")            # Prints to confirm the launch and end of program.

while True:         # Keeps the statement above True and CREATES a loop that stops the code from ending.
    pass       # Dummy statement, does nothing particularlly run-able by th code. Just helps keep the [while] statement true.