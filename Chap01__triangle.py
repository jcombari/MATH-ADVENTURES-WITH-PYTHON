from turtle import *


def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(60)
        triangle()
