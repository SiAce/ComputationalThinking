# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:06:11 2017

@author: 93137
"""

from Tkinter import *
from time import sleep

def main():
    root = Tk()
    c = Canvas(root,width=500,height=1000,bg='white')
    c.pack()
    
    ball = c.create_oval(200,100,300,200,outline = '',fill='Plum')
    c.create_rectangle(0,900,500,1000,outline = '',fill='maroon')    
    
    height = 800.0
    velocity = 0.0;
    dt = 0.05;
    
    while True:
        new_height = height - velocity*dt
        new_velocity = velocity + 9.8*dt
        if (new_height < 100.0 ):
            new_velocity = -new_velocity
            new_height = 100.0
        if (new_height > 800.0 ):
            new_velocity = 0.0
            new_height = 800.0

        d_height = new_height - height
        c.move(ball,0,-d_height)
        c.update()
        
        velocity = new_velocity
        height = new_height
        
        sleep(0.01)
     
main()
