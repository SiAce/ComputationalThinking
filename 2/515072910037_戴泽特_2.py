# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:18:51 2017

@author: siace
"""

n = 1.
total = 0.
while (1 / (2 * n - 1) - 1 / (2 * n + 1) >= 1e-5): #loop stops when the difference of last two terms is less than 0.00001
    total += (-1) ** (n + 1)/(2 * n - 1)
    n += 1
#total ≈ π/4
print total*4