from turtle import *


pathA1= [10,5,11,11,5,10]
#pathA2= [20,10,90,55,60]

#pathB1= [15,45,12,20,55,60,10,90,25]
#pathB2= [90,70,55,42,45,92,22,55,60]


########################################
#Turtle B:
#Turtle Personal rules: 
#If he sees the digit five or two he will rotate 45 to his left.
#If he sees the doesn't see the digit five or two will rotate 45 to his right.
#Any time he sees a number, He will move forward a hundred steps.
#if the number is greater than 50, he will use a green pen. Otherwise he will use a blue pen
#note: he will always start walking towards the top of the screen.

pensize(5)
setheading(90)


def turtle_B(numbers):
    
    for n in numbers:
        if "2" in str(n) or "5" in str(n):
            right(45)
            
        else:
            left(45)
         
        if n>50:
            pencolor("green")
        else:
            pencolor("blue")
      
     
        forward(100)


turtle_B(pathA1)
