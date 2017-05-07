# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:35:42 2017

@author: 93137
"""

from Tkinter import *

root = Tk()
c = Canvas(root,width=1000,height=1000,bg='white')
c.pack()

a = input("Enter the principal:")
i = input("Enter the annual interest rate:")

wealth = []
relative_wealth = []
for n in range(10):
    wealth.append(a*((1 + i)**(n + 1)))
    
for n in range(10):
    relative_wealth.append(wealth[n] / wealth[9] * 800.0)
    
for n in range(10):
    c.create_rectangle(n*90 + 50, 900 - relative_wealth[n], n*90 + 100, 900, fill='gray%s' %(n*7))
    c.create_text(n*90 + 50, 900 - relative_wealth[n], text = '%0.4f' %(wealth[n]), anchor = SW) 
    
root.mainloop()
