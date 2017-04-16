# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:01:47 2017

@author: 93137
"""

def slope(p1,p2):
    '''Calculate the slope of the line of two dots
    p1,p2 are two tuples, each contains the coordinates of one dot
    '''
    try:
        x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]
        slope = float((y2-y1))/(x2-x1)
        return slope
    except ZeroDivisionError:
        return "The slope is infinite"
    except TypeError:
        return "Please input two tuples of coordinates of two dots"
    
def intercept(p1,p2):
    '''Calculate the intercept of line of two dots
    p1,p2 are two tuples, each contains the coordinates of one dot
    '''  
    try:
        x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]
        intercept = (x2*y1-y2*x1)/float((x2-x1))
        return intercept
    except ZeroDivisionError:
        if x1 == 0:
            return "This line is y-axis"
        else:
            return "The line has no point of intersection with y-axis"
    except TypeError:
        return "Please input two tuples of coordinates of two dots"

