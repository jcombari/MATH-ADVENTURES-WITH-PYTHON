from turtle import *
# loop for number of squares

forward(10)
right(10)

for i in range(60):
      
    # loop for drawing each square
    for j in range(4):
          
        # drawing each side of
        # square of length 100 
        fd(100)
          
        # turning 90 degrees
        # to the right
        rt(45)
          
    # turning 6 degrees for
    # the next square
    rt(6)
