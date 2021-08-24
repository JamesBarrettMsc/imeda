from turtle import *


pathA1= [10,5,11,11,5,10]
#pathA2= [20,10,90,55,60]

#pathB1= [15,45,12,20,55,60,10,90,25]
#pathB2= [90,70,55,42,45,92,22,55,60]



###############################
#Turtle D:

#Turtle Personal rules: 
#If he sees the digit odd number rotate 45 to his left.
#If an even number rotate 45 to his right.
#But If he sees the digit five or two he will rotate 45 to his left, he will turn the opposite direction.
#Any time he sees a number, He will move forward a hundred steps.
#if the number is between 10 and 30, he will use a green pen. Otherwise he will use a yellow pen

pensize(5)
setheading(90)

def turtle_D(numbers):
    for n in numbers:
        if n%2==0:
            if "2" in str(n) or "5" in str(n):
                left(45)
            else:
                right(45)
                
        else:
            if "2" in str(n) or "5" in str(n):
                right(45)
            else:
                left(45)
        
        if n>10 and n<30:
            pencolor("green")
        else:
            pencolor("yellow")
            
        forward(100)
            
            
turtle_D(pathA1)

    