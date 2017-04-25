# -*- coding: cp936 -*-
# 输入10个数据,计算并输出这组数据的标准离差.
 
import math

# 如何存储10个数据?用10个变量吗?
data = []
s = 0
for i in range(10):
    x = input("输入数据：")
    data = data + [x]
    s = s + x

x_bar = s / 10.0

s2 = 0
for d in data:
    s2 = s2 + (d - x_bar)**2
    
stdv = math.sqrt(s2 / 10.0)

print "标准离差:",stdv
