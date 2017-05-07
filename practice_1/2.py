#Purpose: Calculate a piecewise function
#Author: SiAce
#Date: 3/10/2017

from math import *

print "Enter the value of x:"
x = input()
if (x>0):
    f = (sin(x)**2+cos(x)+1)**3-3*(sin(x)**2+cos(x))
elif (x<0):
    f = 4*sin(x)**2+4*cos(x)-1
else :
    f = pi # When x = 0
print "f(x) =",f
    
