# Engineering 4 Notebook
This is where all my stuff will go!
## Headless
### Code
### Lessons Learned
For the Headless assignment we had to create a graph that showed the x value of the accelerometer, and then had to make it work with a battery for its external power source. We had trouble creating code that created the graph but then foud some resources on google as well as help from others in class to create code to allow it to run on a battery. 
## GPIO-Pins I2C
### Code
### Lessons Learned
For this assigment we had display the x, y, and z values using an accelerometer. 
## GPIO-Pins Flask
### Code
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	led1 = GPIO.input(17)
	led2 = GPIO.input(18)
	checked1 = ""
	checked2 = ""
	if request.method == "POST":
		if('hiddenElement1' in request.form):
			if(led1 == True):
				GPIO.output(17, GPIO.LOW)
				msg1 = "LED 1 is off"
				checked1 = ""
			else:
				GPIO.output(17, GPIO.HIGH)
				msg1 = request.form.get("submitBtn")
				checked1 = "checked"
			if(led2 == True):
				msg2 = "LED 2 is on"
				checked2 = "checked"
			else:
				msg2 = "LED 2 is off"
				checked2 = ""
		else:
			if(led2 == True):
				GPIO.output(18, GPIO.LOW)
				msg2 = "LED 2 is off"
				checked2 = ""
			else:
				GPIO.output(18, GPIO.HIGH)
				msg2 = request.form.get("submitBtn")
				checked2 = "checked"
			if(led1 == True):
				msg1= "LED 1 is on"
				checked1 = "checked"
			else:
				msg1 = "LED 1 is off"
				checked1 = ""
	else:
			GPIO.output(17, GPIO.LOW)
			GPIO.output(18, GPIO.LOW)
			msg1 = "LED 1 is off"
			msg2 = "LED 2 is off"
			checked1 = ""
			checked2 = ""
	return render_template(
			"index.html",
			msg1=msg1,
			msg2=msg2,
			checked1=checked1,
			checked2=checked2)
if __name__ == "__main__":
		app.run(host="0.0.0.0", port=80)
### Lessons Learned
For this assigment we had to create an html page that allowed us to use buttons to control an LED to turn on and off. We had issues as when we hit the button twice it wouldn't turn off we adjusted our code and made it color full as well as being able to control the LED from our phones. 
## Hello Flask
### Code
### Lessons Learned
In this assigment we craeted a web page that we coded to say Hello world we didn't have issues completing this assigment.
## SSH
### Code
### Lessons Learned
Using the Pi Ip address we were able to turn two LEDs on and off which didn't take very long. 
## Python
### Code
### Lessons Learned
For this assigment we used bash to code 2 LEDs to blink 10 times before automatically turn off. 
## Bash
### Code
### Lessons Learned

## MSP
### Code
### Lessons Learned
## Strings and Loops
### Code
### Lessons Learned
## Forks and Clones
### Code
### Lessons Learned
## Hello Git 
### Code
### Lessons Learned
 
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
## Hello Python
### Code
##### [https://github.com/cmunro97/Engineering_4_Notebook/blob/master/Python/lesson00.py]
    str = "Hello World!"

    for x in range(0,10):
        print (str)
### Lessons leadrned
