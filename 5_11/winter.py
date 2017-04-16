from Tkinter import *
import random

def set_background():
    """Set the background of the canvas"""
    c.create_rectangle(0,0,1000,600,fill='lightblue')
    
def draw_sun():
    """Draw the sun on the canvas"""
    c.create_oval(20,20,100,100,fill='yellow')
    
def draw_snowman():
    """Draw the snowman on the canvas"""
    c.create_oval(175,350,275,450,fill='white')
    c.create_oval(150,450,300,600,fill='white')
    c.create_oval(200,375,210,385,fill='black')
    c.create_oval(240,375,250,385,fill='black')
    c.create_oval(215,390,235,410,fill='red')
    c.create_arc(200,375,250,425,start=225,extent=90,style='arc',width=4,outline='brown')
    c.create_rectangle(200,300,250,350,fill='blue') 
    c.create_rectangle(190,350,260,360,fill='blue')
    c.create_line(170,470,225,490,width=20,fill='red')
    c.create_line(280,470,225,490,width=20,fill='red')
    c.create_line(225,490,225,550,width=20,fill='red')
    c.create_line(170,490,120,430,width=10,fill='brown')
    c.create_line(140,450,140,430,width=10,fill='brown')
    c.create_line(140,450,120,450,width=10,fill='brown')
    c.create_line(280,490,330,430,width=10,fill='brown')
    c.create_line(310,450,310,430,width=10,fill='brown')
    c.create_line(310,450,330,450,width=10,fill='brown')
def draw_tree(x=0,y=0):
    """Draw the tree on the canvas"""
    draw_triangle(x,y,size=80)
    draw_triangle(x,y+60,size=100)
    draw_triangle(x,y+140,size=120)
    c.create_rectangle(x-20,y+250,x+20,y+450,fill='brown')
    
def draw_snow(x=0,y=0):
    """Draw the snow on the canvas"""
    c.create_oval(x,y,x+10,y+10,fill='white')
    
def draw_triangle(x=0,y=0,size=50,color='darkgreen'):
    """Draw a triangle"""
    c.create_polygon(x,y,x-size,y+size,x+size,y+size,fill=color)


root = Tk()
c = Canvas(root,width=1000,height=1000,bg='white')
c.pack()

set_background()
draw_sun()
draw_snowman()
draw_tree(500,150)
draw_tree(600,150)
draw_tree(700,150)
draw_tree(800,150)
draw_tree(900,150)
for i in range(500):
            draw_snow(random.uniform(0, 1000),random.uniform(0, 1000))

root.mainloop()
    




