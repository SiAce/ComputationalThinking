# -*- coding: cp936 -*-
# ����10������,���㲢����������ݵı�׼���.
 
import math

# ��δ洢10������?��10��������?
data = []
s = 0
for i in range(10):
    x = input("�������ݣ�")
    data = data + [x]
    s = s + x

x_bar = s / 10.0

s2 = 0
for d in data:
    s2 = s2 + (d - x_bar)**2
    
stdv = math.sqrt(s2 / 10.0)

print "��׼���:",stdv
