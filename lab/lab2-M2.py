# -*- coding: cp936 -*-

# ����������n��<7�������n���ɴ�д��ĸ����A��ʼ����ɵ����������С�
# ���磺����3�����
# A B C 
# D E
# F

n = input("������һ��С��7����Ȼ����")
a = ord('A')
k = 0
for i in range(n,0,-1):
    for j in range(i):
        print chr(a+k),
        k = k + 1
    print

