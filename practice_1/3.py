#Purpose : Calculate the standard deviation of ten numbers 
#Author: SiAce
#Date: 3/10/2017

from math import *

print "Enter ten numbers:"
a = []
b = [0.0]
total = 0.0
average = 0.0
add = 0.0
standardDeviation = 0.0 #Initialization
for i in range(10):
    b[0] = input()#Use array b as a buffer
    a = a + b #Put the input into the array a
for i in range(10):
    total += a[i] #Calculate the total 
average = total / 10 #Calculate the average
for i in range(10):
    add += (a[i]-average)**2 #Calculate the average
standardDeviation = sqrt(add/10)  #Calculate the standardDeviation

print "The standard deviation of these ten numbers is %f" %standardDeviation
    
