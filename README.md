# Engineering 4 Notebook
## Hack Your Stuff
### Code
#### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/hackyourstuff.py]
### Lessons Learned
In this assignment, we had to turn a window alarm on and off using our pi. This assignment brought back some funny memories for us. On the first day of engineering, freshman year, we had been looking at the bins in the back and we ended up triggering one of these window alarms. It took us a solid 10 seconds of screeching beeps before we got it turned off. So for this assignment we tried to minimze the number of times we had to test out the alarm and hear its noise. We struggled the most with the wiring on this assignment. The alarms in the bin were in all sorts of conditions with different parts missing and added. Once we found an alarm that was working we took it apart so it could work with the pi. 
## Pi Camera
### Lessons Learned 
The Pi Camera assignment was a 3 part assignment. The first part simple puts the camera's view onto the monitor. The second part includes effects and must capture images. In the third part we recorded a video and converted it to a mp4 file.
#### Camera Test 1
##### Code [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/camera_test01.py]
    from picamera import PiCamera
    from time import sleep

    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
#### Camera Test 2 
##### Code [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/camera_test02.py]
Here are some of the images we captured:

https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/filename1.jpg
https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/filename2.jpg
https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/filename4.jpg
#### Camera Test 3
Here is the video we took using our Pi Camera:

https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/videotest.mp4
##### Code [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/camera_test03.py]

## Headless
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/headless.py]
### Lessons Learned
For the Headless assignment we had to create a graph that showed the x value of the accelerometer, and then had to make it work with a battery for its external power source. We had trouble creating code that created the graph but, after lots of searching, we found some resources on google which helped us. We found that the best way to run the program at startup was to type "nano .bashrc" into terminal and then edit it to say "Echo Runing at boot" and "sudo python3 (code location and name)." Once we rebooted it the code ran imediately. The battery connection was also very straightforward, though we ended up borrowing the battery of another group becasue the first one we grabbed wasn't charged.
## GPIO-Pins I2C
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/I2C%2Cpy.py]
### Lessons Learned
For this assigment we had display the x, y, and z values using an accelerometer. It was our first time using an accelerometer and we had some trouble setting it up because we had confused the SDA and SCL wirings. At first it would not display the data points although it was taking data. It turned out that we had not been clearing the screen. Once we did this it worked perfectly.
## GPIO-Pins Flask
### Code
[https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/Flask/gpio/app.py]
### Lessons Learned
For this assigment we had to create an html page that allowed us to use buttons to control an LED to turn on and off. It took as a long time (and of course lots of googling) to fully understand get and post and figure out how to use them. When we hit the button twice it wouldn't turn off and the buttons would sometimes affect each other when they shouldn't be. We poured over our code and analyzed its details to find that we had mixed up the names of the buttons in our loop. We adjusted our code and once we had figured out the main code we played around with the color to make it more aesthetically pleasing. We were then able to control the LED from our phones. We could't use our chrombooks because of administrative restrictions on them.
## Hello Flask
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/Flask/hello_world/app.py]
### Lessons Learned
In this assigment we created a web page that we coded to say "Hello World." This was the first time we had to use "sudo" to run a command. That's always what we try now when a command of ours isn't doing what it needs to. Learning about sudo has been especially helpful in doing more complicated stuff with out pi, such as running at startup and troubleshooting vague issues.
## SSH
### Code
### Lessons Learned
We used the Pi IP address app that it gave us and  were able to turn two LEDs on and off from a phone after typing very simple code. It was able to work over the wifi signal instead of being concted like in the past. We learned that SSH won't work if you are on different wifi networks or are trying to use cellular data to connect. Using our phones to do coding was really cool, especially since we didn't think they were capable of that.
## Python
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/gpio_18.py]
### Lessons Learned
This assignment was like the previous assignment, as we had to code 2 LEDs to blink 10 times before automatically turning off. The difference was that this was in python rather than bash. This also went quickly as it was similar to the previous assignment and the wiring was the same. A significant difference was that you refer to the pins as different numbers. We also initially had trouble with warnings, but once we ignored them it worked smoothly.
## Bash
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Scripts/blink.sh]
### Lessons Learned
Bash allowed us to wire LEDs onto a Pi for the first time which was supprisingly easy. We didn't expect the wiring to be so similar to arduino but at the same time it makes sense. The code was pretty straightforward so we completed the assignment fairly quickly and it stopped after blinking 10 times.
## MSP
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/hangman2.py]
### Lessons Learned
We struggled with this assigment because our code did not draw the man corectly. It would draw his limbs to the side so that it was off center and sometimes would add extra lines. We had to do a lot of googling and asked a lot of questions. It took us a long time to adjust the code and write it correctly but with help we were able to figure it out. One of our major issues was that we were using the wrong numbers so it was doing the various lines at the wrong time. We made our hangman unique by having his limbs be in a comical dancing position. Once we had worked out all the kinks, we had a lot of fun testing it out and playing hangman.
## Strings and Loops
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/split.py]
### Lessons Learned
Strings and loops was an exercise on how to print lines in python. We had little trouble with this assigment, but, as usual, our  error was a simple typing error: a comma in the wrong place.
## Forks and Clones
### Lessons Learned
We created a coolrepo page on github and were able to add some fun facts about ourselves. We forked a page that Jack had created then added our information after we had to clone that page and add it to our own github page. We initially couldn't get to the necessary page but it turned out to just be a spelling error in one of our commands.
## Hello Git 
### Lessons Learned
WE STARTED PYTHON and now it is time to learn how to push our code to github where we can share it with everyone and access it from anywhere!! The directions were straighttforward and we had no issues pushing our first projects. This assaignment remained an incredibly helpful tool until we memorized the steps to pushing our code. We found it really interesting how the pi could interact with the real world through this.
## Quadratic Solover
### Code 
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/Quadsolver.py]
    import math

    def myFunction(a,b,c):
        return b**2-4*a*c

    def mathFunction(a,b,c):
        return[(-b+math.sqrt((b**2)-(4*(a*c))))/(2*a),(-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)]


    a = int(input("Enter the coefficients of a: "))
    b = int(input("Enter the coefficients of b: "))
    c = int(input("Enter the coefficients of c: "))


    d = myFunction(a,b,c) #b**2-4*a*c # discriminant

    if d < 0:
        print ("This equation has no real solution")
    elif d == 0:
        print ("this equation has one solution: "), x
    else:
        print ("This equation has two solutions: ", mathFunction(a,b,c)[0], " or", mathFunction(a,b,c)[1])


### lessons learned
This lesson we used Mathmatica to solve quadratic equation. At first, the code we had written would only multiply the three inputed numbers. After some troubleshooting it would do the quadratic correctly. The program would sometimes give us answers that weren't solutions to the quadratic. We fixed this issue by introducing "d" so it could identify nonreal answers. 
## Calculator 
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/calc.py]
    a = input("Type a number")
    b = input("type a second number")
 

    def doMath(x,y,z):
        x = int(x)
        y = int(y)
        if z==1:
            return(str(x+y))
        if z==2:
            return(str(x-y))
        if z==3:
            return(str(x*y))
        if z==4:
            return(str(round (x/y,2)))
        if z==5:
            return(str(x%y))

    print("Sum:\t\t" + doMath(a,b,1))
    print("Difference:\t\t" + doMath(a,b,2))
    print("Product:\t\t" + doMath(a,b,3))
    print("Quotient:\t\t" + doMath(a,b,4))
    print("Modulo:\t\t" + doMath(a,b,5))
### Lessons learned
The calculator alowed us as the users to input 2 numbers that would then be added, subtracted, divided, and multiplied. At first our code didn't allow for us to input a number but after trouble shooting we fixed it. Our issue was that we didn't write code that would ask for an input. We then had to figure out how to make the numbers round, though this was quite doable with some googling. 
## Dice Roller
### Code 
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/diceroller3.py]
    from random import randint

    print ("Do you want to roll? (Y)es or (N)o")
    answer = input()
    while answer.lower()[0] == "y":
        num1 = randint(1,6)
        print ("You rolled a", num1)
        print ("Do you want to roll? (Y)es or (N)o")
        answer = input()
### Lessons learned
Unlike the arduino, with the Pi we are able to apply diffrent applications such as Mathmatica which we were introduced to in this assigment. For this assigment we had trouble creating a dice that rolled randomly. At first, it rolled a six every time. By adding the first line of code it became random. At first, we also had trouble printing the number that was rolled because we had initially put it inside the parentheses. 
## Hello Python
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/Engineering_4_Notebook/Scripts/hello_world.sh]
### Lessons learned
This was our first lesson using a Raspberry Pi which was really exciting. It was very helpful to see the similarities with arduinos, the lesson was very helpful and we were quick to learn how to code a loop on the Pi. We also were able to solder the raspberry Pi directly which was interesting as we had only ever soldered wires together.
