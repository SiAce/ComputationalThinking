# -*- coding: cp936 -*-

# 输入正整数n（<7），输出n行由大写字母（从A开始）组成的三角形阵列。
# 例如：输入3，输出
# A B C 
# D E
# F

n = input("请输入一个小于7的自然数：")
a = ord('A')
k = 0
for i in range(n,0,-1):
    for j in range(i):
        print chr(a+k),
        k = k + 1
    print

