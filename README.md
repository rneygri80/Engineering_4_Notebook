# Engineering 4 Notebook

## Headless
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/headless.py]
### Lessons Learned
For the Headless assignment we had to create a graph that showed the x value of the accelerometer, and then had to make it work with a battery for its external power source. We had trouble creating code that created the graph but then foud some resources on google as well as help from others in class to create code to allow it to run on a battery. 
## GPIO-Pins I2C
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/I2C%2Cpy.py]
### Lessons Learned
For this assigment we had display the x, y, and z values using an accelerometer. 
## GPIO-Pins Flask
### Code
[https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/Flask/gpio/app.py]
### Lessons Learned
For this assigment we had to create an html page that allowed us to use buttons to control an LED to turn on and off. We had issues as when we hit the button twice it wouldn't turn off we adjusted our code and made it color full as well as being able to control the LED from our phones. 
## Hello Flask
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/Flask/hello_world/app.py]
### Lessons Learned
In this assigment we craeted a web page that we coded to say Hello world we didn't have issues completing this assigment.
## SSH
### Code
### Lessons Learned
Using the Pi Ip address we were able to turn two LEDs on and off which didn't take very long. 
## Python
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/gpio_18.py]
### Lessons Learned
For this assigment we used bash to code 2 LEDs to blink 10 times before automatically turn off. 
## Bash
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Scripts/blink.sh]
### Lessons Learned

## MSP
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/hangman2.py]
### Lessons Learned
We struggled with this assigment as our code did not draw the man corectly and it took us a long time to ajust the code to write it correctly we used google quite a bit and asked people who had already finished. We also had trouble with the computer knowing if the letter typed was in the word however after a while we fixed our code. 
## Strings and Loops
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/split.py]
### Lessons Learned
Strings and loops was and excersize of how to print lines in python we had little trouble with this assigment.
## Forks and Clones
### Lessons Learned
We created a coolrepo page on github and were able to add some fun facts about ourselves. We forked a page that Jack had created then added our information after we had to clone that page and add it to our own github page.
## Hello Git 
### Lessons Learned
WE STARTED PYTHON and now it is time to learn how to push our code to github where we can share it with everyone and access it from anywhere!! The directions were straitforward and we had no issues pushing our first projects.
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
This lesson we used mathmatica to solve quadratic equetion. At first the code we had written would only multiply the three inputed numbers after trouble shooting it would do the quadratic however even if it was not a quadratic it would say that it was.  
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
The calculator alowed us as the users to input 2 numbers that would then be added, subtracted, divided, and multiplied. At first our code didn't allow for us to input a number but after trouble shooting we fixed it, then we had to figure out how to make the numbers round which we easily found code for by googling. 
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
Unlike the arduino with the Pi we are able to aply diffrent applications such as mathmatica which we were introduced to in this assigment. For this assigment we had trouble createing the a dice that rolled randomly at first it rolled a six every time. by adding the first line of code it became random we also had trouble printing the number that was rolled because we had it inside the parentheses at first. 
## Hello Python
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/Engineering_4_Notebook/Scripts/hello_world.sh]
### Lessons leadrned
This was our first lesson using a pi and it was very helpful to show similarities with arduino, the lesson was very helpful and we were quick to learn how to code a loop on the Pi. We also were able to souder the raspberry Pi which was intresting as we had only ever soudered wires together.
