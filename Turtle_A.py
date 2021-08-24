from turtle import *


pathA1= [10,5,11,11,5,10]
#pathA2= [20,10,90,55,60]

#pathB1= [15,45,12,20,55,60,10,90,25]
#pathB2= [90,70,55,42,45,92,22,55,60]

########################################
#Turtle A; 
#Turtle Personal rules: 
#When he sees a number that is less than the last number he seen he will turn left 45 degrees.
#When he sees a number that is greater than or equal to the last number he has seen he will turn right 45 degrees. 
#Any time he sees a number, He will move forward a hundred steps.
# if it is an even number. The turtle will use a green pen, Otherwise he will use a red pen
# note: if he has not been shown a number he will compare next number against the number zero.
# note: he will always start walking towards the top of the screen.


pensize(5)
setheading(90)

def turtle_A(numbers):
    
    num=0
    for n in numbers:
        if n<=num:
            left(45)
        else:
            right(45)
            
        if n%2==0:
            pencolor("green")
        else:
            pencolor("red")
                
        forward(100)
        num=n
        

import time
time.sleep(3)   

turtle_A(pathA1)
