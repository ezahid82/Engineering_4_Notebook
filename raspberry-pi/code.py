# type: ignore

import time
import board
import digitalio
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
displayio.release_displays()

# assigning  pico pins to the accelerometer pins
sda_pin = board.GP16   # sda = Serial Data
scl_pin = board.GP17   # scl = Serial Clock
i2c = busio.I2C(scl_pin, sda_pin) 
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

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

           # create the display group
        splash = displayio.Group()

        # A line is called using the endpoints of the line, (x1,y1) and (x2,y2)
        hline = Line(64,0,64,64, color=0xFFFF00)
        splash.append(hline)
        
        # A second line is called to make the horizontal line
        vline = Line(0,32,128,32, color=0xFFFF00)
        splash.append(vline)
        
        # A circle is called using the center point (x,y) and the radius (r) 
        circle = Circle(64, 32, 4, outline=0xFFFF00)
        splash.append(circle)

        triangle = Triangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), outline=0xFFFF00)
        splash.append(triangle)
        # send display group to screen
        display.show(splash)

        
        
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




 



