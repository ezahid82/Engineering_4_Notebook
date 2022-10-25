# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Launchpad Part 1 (Countdown)

### Assignment Description

the **countdown** assignment was intended to test a program that would fix the broken space launch pad and accuratly allow the astronauts to launch a ship at the end of the countdown

### Evidence 

![the countdown ran completely](./images/launchpad%20countdown.PNG)

### Wiring

no wiring was needed other than a pico baord connection to the device. 

### Code 

[Launch Pad Part One.](raspberry-pi/Launch%20Pad%20Part_1)

### Reflection

This assignment was challenging because of the language and making the [**for-loop**] encrement the numebers decreasing from [one] to [10]. After some testing, I was able to figure out how to increment the numbers negatively.



&nbsp;


## Launch Pad Part 2 (lights)

### Assignment Description

This assignment was to add **LEDs** to the countdown so that the astronauts are aware of 

### Evidence 

![Countdown with LEDs](images/Launch%20Pad%20Part%202%20%5Bevidence%5D.gif)

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

![Launch Pad Part 2 (wiring)](images/Launch%20Pad%20Part%202%20%5Bwiring%5D.jpg)


### Code

[Launch Pad Part 2 (code)](raspberry-pi/Launch%20Pad%20Part_2)

### Reflection

This assignment was challenging in the sense that getting the countdown of the launch to work. It was solved using an if statment with a range **"equation"** (x <= 10 and x >= 1) to make the *led* turn on and off. I learned that if you add a [while] statement with [pass] as a *dummy* code line that would keep the code running continuesly.


&nbsp;




## Launch Pad Part 3 (button)


### Assignment Description

The **button** assignement was intended to add a manual lanuch system that would allow the countdown to start only by command. This assignment would all the rocket to stay put until all other actions have been completed and a given command by the push of the button would allow it to launch.

### Evidence 

![the button launch](images/Launch%20Pad%20Part%203%20gif%20(Button).gif)


### Wiring

![launch pad part 3 (button) wiring](images/Launch%20Pad%20Part%203%20%5Bwiring%5D.jpg)


### Code

[launch pad part 3 (button) code](raspberry-pi/Launch%20Pad%20Part_3)



### Reflection

This assignement was challenging with getting the button statements and variables. It was solved by getting the dircetion of the **botton** *input* and simply adding a [**while**] loop and using an [**if**] statment to check *if* the **button** has been pressed. I was able to learn that you don't need all the pins of the button to make it function as intended. Only two wires on the same side would be enough. Secondly, some [**GP**] pins share the same **PWM** frequency.


&nbsp;



## Launch Pad Part 4 (servo)

### Assignment Description

This assignment made the engineers launch the spaceship from a launch pad that could move and let the rocket go as it launched by the end of the countdown. 


### Evidence 

![Launch Pad Part 4 (Servo)](images/Launch%20Pad%20Part%204%20%5Bevidence%5D.gif)

### Wiring

![Launch Pad Part 4 (wiring)](images/Launch%20Pad%20Part%204%20%5Bwiring%5D.gif)


### Code

[launch pad part 4 (code)](raspberry-pi/Launch%20Pad%20Part_4)

### Reflection

This assignment was challenging in that it was difficult in getting the servo to work. It was however much easier because the code was similar to the **led** and **button**. The Servo at somepoint wouldn't spin 180 degrees and wouldn't reset after it had finished running. IT was solved by testing different angles, and getting the servo to spin back to (**0**) after it was done.

&nbsp;





## Crash Avoidance Part 1 (Accelerometer)

### Assignment Description

This assignment will take an accelerometer and would return you the **X, Y,** and **Z** values. The acceleromter would update every second to *actively* display the coordinates.

### Evidence 

![accelerometer gif](images/crash%20avoidance%20(accelerometer)%20%5Bevidence%5D.gif)

### Wiring

![accelerometer wiring](images/Crash%20Avoidance%20(accelerometer)%20%5Bwiring%5D.jpg)

### Code

[Crash Avoidance (Accelerometer) [code]](raspberry-pi/Crash%20Avoidance%20(accelerometer))

### Reflection
This assignment was challenging with getting the variables **X, Y,** and **Z** to start to output correct numbers. At first, I had a hard time getting each to be displayed one on top of the other. It was solved by using numbers to identify *X,Y,Z*. I learnt that if you use an **if-string**, it is much easier to have variables and text as you would put the varliable the **{}** and the text *string* can go on the outide of the brackets, but inside the quote marks.

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;




## Crash Avoidance Part 2(light + powerboost)

### Assignment Description

the purpose of this assignment is to make the accelerometer light up when it is *turned* **90 degrees** and then be *"headless"* by being *connected* to a **LiPo battery**.

### Evidence 

![light + powerboost (gif)](images/Crash%20Avoidance%20(light%20+%20powerboost)%5Bevidence%5D.gif)

### Wiring

![crash avoidance part 2 wiring](images/Crash%20Avoidance%20(light%20+%20powerboost)%20%5Bwiring%5D.jpg)

### Code

 [light and powerboost (code)](raspberry-pi/Crash%20Avoidance%20(light+powerboost))

### Reflection

This assignement wasn't as challengeing since it required the previous code and only required *added* code. An **If-statement** was added to the code which made the accelerometer read in *90 degrees* and if it was **true**, the **red led** would turn on. On the outside, the wiring was changed only with the *LED* added to **GP 15** and the cord that connected it to the computer was replaced with a **powerboost 500C** that powered teh whole circuit.

&nbsp;




## Crash Avoidance Part 3(OLED Screen)

### Assignment Description

This assignment was to 

### Evidence 

![Crash Avoidance Part 4 evidence](images/Crash%20Avoidance%20(OLED%20Screen)%20%5Bevidence%5D.gif)

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code

[OLED Screen (code)](raspberry-pi/Crash%20Avoidance%20part%203%20(OLED%20Screen))

### Reflection

This assignment was only adding new parts to the previous wiring. It was easy to understand that by putting the (**SDA**) and (**SCL**) pins behind the accelerometer, you can connect those pins to the *OLED Screen*. I was difficult to get the LED Screen to display the numbers, as it would always cuase a syntax error. It was resolved by placeing the correct order of code in order to make the *Pico* read in which device was feeding it data.

&nbsp;




## Landing Area Part 1 (functions)

### Assignment Description

This assignment measures the **area** of a triangle while given *three different* coordinates in (x,y) form. It runs a function that converts the inputed String into numbers that would be easily used to calculate the area by using the equation of a triangle with vertices.


### Evidence 

![Functions calculating area](images/Landing%20Area%20Part1%20(functions).gif)

### Wiring

none needed for this part 

### Code

[functions](raspberry-pi/Landing%20Area%20Part%201%20(functions))

### Reflection

This assignement was challenging in first turning the inputted vales which are originally in **String** form, to numbers that could be used to calculate the **area**. It was solved by using a **float()** method. One thing new I learnt was that by using a **split()** method, you could *split* a character based on agiven input. In this case it was **[code].split(" , ")** to separate the string at the comma.


&nbsp;



## Landing Area Part 2 (plotting)

### Assignment Description

This assignment is intended to make the previously entered coordinates, **plotted** on the *OLED Screen*. The screen consists of X and Y-axis that in the center *(64,32)* is the location of the base. The triangle is then displayed relative to the base on the **map**.

### Evidence 

![Landing Area (plotting) [gif]](images/Landing%20Area%20(plotting).gif)

### Wiring

![Landing Area (plotting) [wiring]](images/Landing%20Area%20(plotting)%20%5Bevidence%5D.JPG)

### Code

[Landing Area (plotting) [code]](raspberry-pi/Landing%20Area%20Part%202%20(plotting))

### Reflection

As I was trying to make the coordinates and shape plotted on the **OLED Screen**,  the plots wouldn't render in because of some problem the OLED Screen faced with not displaying the image. It was discovered that while printing the triangle, only the coordiantes inputted would be calculated, but it had no way of know where to put it or what to do with it. It was solved by assigning the coordinates *before* the **splash** which would display it on the screen, and they were moved because the **base** was in the *center* of the screen (64,32), while to OLED Screen started its coordinates from top left corncer (0,0). From this experience, I learnt how to make an OLED Screen work with math and calculations on a graph. It was clear that the screen wouldn't run without **splash**.


&nbsp;



## Morse Code (Translation)

### Assignment Description

This assignment was intended to turn a message into it's morse code pattern. The code uses a **for loop()** to keep the code running continously and uses a specific *string*, **("-q")**, to break from the loop. 

### Evidence 

![Morse Code (translation) [gif]](images/Morse%20Code%20(Translation)%20%5Bevidence%5D.gif)

### Wiring

none needed for this assignment

### Code

 [morse code (translation)[code]](raspberry-pi/Morse%20Code%20(translation))

### Reflection

This assignemnt was challenging with getting the **Morse Code** code print correctly. I was solved by making the variable **message** to store the letters and use the corresponding *Morse Code* to print out. One thing I learnt was that by using **break**, you can exit a while loop by a combination of **if() statements**.

&nbsp;




## Morse Code (Transmission)

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;





## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;



## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
 [Battery Charging](https://www.chargingchargers.com/tutorials/charging.html)
 
### Test Image
![Picture Name Here](images/Github%20Repositry%20test%20gif.gif)  

### Test GIF
![Picture Name Here](images/Github%20Repositry%20test%20image.jpg)  

