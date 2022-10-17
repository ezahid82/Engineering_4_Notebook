# type: ignore

import time
import board
import digitalio
import adafruit_mpu6050
import busio
import board
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle


# assigning  pico pins to the accelerometer pins
sda_pin = board.GP16   # sda = Serial Data
scl_pin = board.GP17   # scl = Serial Clock
i2c = busio.I2C(scl_pin, sda_pin) 
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP12)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)









def triangle_area(x1y1,x2y2,x3y3):   # makes a function with parameters for x,y coordinates


    try:    # tests a block of code for errors

    # splits the x1y1 coordinates into separate variables like x1, y1.
        x1y1 = x1y1.split(",")
        x2y2 = x2y2.split(",")
        x3y3 = x3y3.split(",")

    # turns the inputed string in x1 y1 into number forms.
        x1 = float(x1y1[0])
        y1 = float(x1y1[1])
        x2 = float(x2y2[0])   #[0] means that after every comma, the number order always becomes 0 and goes on before another comma is added
        y2 = float(x2y2[1])   #[1] means that the next inputed string you be under value 1
        x3 = float(x3y3[0])
        y3 = float(x3y3[1])

        area = (1/2)*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))   # The equation for calucalting the area of a triangle with three vertecies

        return area

    except:   # lets you handle the error
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")
        area = 0
        return area

# asks the user for three x,y coordinates 
while True:

    print ("please enter the first coordinates in form x,y: ")
    x1y1 = input()
    print ("please enter the second coordinates in form x,y: ")
    x2y2 = input()
    print ("please enter the third coordinates in form x,y: ")
    x3y3 = input()

    area = triangle_area(x1y1,x2y2,x3y3)   # assigns the coordiantes to area

    if area == 0:
        continue
    else:  # prints out the calculated area
        area = print(f" the Area of {x1y1} + {x2y2} + {x3y3} is {area} square km.")




    # create the display group
    splash = displayio.Group()

    # add title block to display group
    title = "ANGULAR VELOCITY"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)    

    title = "ANGULAR VELOCITY"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=15)
    splash.append(text_area)

    # you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
    # Don't forget to round the angular velocity values to three decimal places

    # send display group to screen
    display.show(splash)