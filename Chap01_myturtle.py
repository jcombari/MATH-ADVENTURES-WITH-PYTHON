from turtle import *

forward(100)
shape('turtle')

right(45)
forward(150)

for i in range(4):
    forward(100)
    right(90)

def square():
    for i in range(4):
        forward(100)
        right(90)

shape('square')
# loop for number of squares
for i in range(60):
      
    # loop for drawing each square
    for j in range(4):
          
        # drawing each side of
        # square of length 100 
        fd(100)
          
        # turning 90 degrees
        # to the right
        rt(90)
          
    # turning 6 degrees for
    # the next square
    rt(6)



