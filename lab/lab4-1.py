# -*- coding: cp936 -*-

# 输入本金a和年利率i,计算今后n年的增值情况:a*((1+i)**n)
# 并用柱状图表示

from Tkinter import *

def getInput():
    a = input('输入本金：')
    i = input('输入年利率：')
    n = input('输入年：')
    return a,i,n

def initCanvas(n):
    r = Tk()
    w1 = (n+1)*(20+30)
    w = 10 + w1 + 10
    h = 10 + 20 + 400 + 10
    c = Canvas(r,width=w,height=h,bg='white')
    c.pack()
    c.create_line(10,10,w1+10,10)
    c.create_line(10,430,w1+10,430)
    return r,c
    
def drawBar(c,a,i,year,limit):
    money = a*((1+i)**year)
    x1 = 20 + year * 50
    y1 = 430 - money * 400 / limit
    x2 = x1 + 30
    y2 = 430
    c.create_rectangle(x1,y1,x2,y2,fill='green')
    m = "%-0.2f" % money
    c.create_text(x1,y1-20,text=m,anchor=NW)
    
def main():
    a,i,n = getInput()         # 输入本金利率和年数
    
    limit = a*((1+i)**n)       # 确定纵坐标上限

    r,c = initCanvas(n)        # 创建窗口和画布
    
    for year in range(n+1):    # 画n+1根柱子
        drawBar(c,a,i,year,limit)

    r.mainloop()
        
main()
