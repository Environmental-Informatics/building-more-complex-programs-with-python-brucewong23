####################
# Header
# Jan. 22 2020
# Shizhang Wang
# 0027521360
# this program draws flowers as shown in exercise 4.2 in thinkpython 2
"""
Created on Wed Jan 22 14:28:19 2020

@author: wang2846
"""

import turtle
import numpy as np
bob = turtle.Turtle()

def polyline(t, length, n, angle):
    print(t)    # create turtle window with appropriate input, i.e. bob
    for i in range(n):
        t.fd(length)    # draw forward length input as increment
        t.lt(angle)    # left turn angle input
        
def arc(t, r, a):
    arc_length = 2*np.pi*r*(abs(a)/360.0)
    n = int(arc_length/4)+3    # determine number of increments, add 3 
    # to make sure there's at least 3 sides
    length = arc_length/n    # determine drawing length increment
    angle = a/n    # determine turning angle increment
    t.lt(angle/2)   # reduce effect of linear approximation error
    polyline(t, length, n, angle)   # polyline was called with n small 
    # increment to draw an arc
    t.rt(angle/2)
    
def one_petal(t, r, a):
    for i in range(2):  # two arcs form a petal
        t.lt(180 - a)  #  to draw the same arc but at opposite direction
        arc(t, r, a)
        
def flower(t, r, a, petals):
    for i in range(petals):     # how many petals to draw
        one_petal(t, r, a)
        t.lt(360.0/petals)
        
def move(t, length):    # move the pen w/o drawing anything
    t.pu()
    t.fd(length)
    t.pd()
    
move(bob, -200)     # locate, draw then relocate and draw
flower(bob, 60, 60, 7)
move(bob, 120)
flower(bob, 40, 80, 10)
move(bob, 120)
flower(bob, 140, 20, 20)
turtle.mainloop() # hold until user close it