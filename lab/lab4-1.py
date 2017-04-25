# -*- coding: cp936 -*-

# ���뱾��a��������i,������n�����ֵ���:a*((1+i)**n)
# ������״ͼ��ʾ

from Tkinter import *

def getInput():
    a = input('���뱾��')
    i = input('���������ʣ�')
    n = input('�����꣺')
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
    a,i,n = getInput()         # ���뱾�����ʺ�����
    
    limit = a*((1+i)**n)       # ȷ������������

    r,c = initCanvas(n)        # �������ںͻ���
    
    for year in range(n+1):    # ��n+1������
        drawBar(c,a,i,year,limit)

    r.mainloop()
        
main()
