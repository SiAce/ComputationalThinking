# -*- coding: cp936 -*-

# ����һ����λ��n���ҳ�100��n֮����������������������x��
# x����ȫƽ��������x����λ������ͬ����144��676�ȡ�
# ���������x����ͳ�Ƹ�����

from math import sqrt

def getInput():
    n = input("������һ����λ����")
    while n<100 or n>999:
        print "��������"
        n = input("������һ����λ����")
    return n

def perfect(x):
    i = int(sqrt(x))     # ��x��ƽ������ȡ��
    if i**2 == x:        # ��֤x�Ƿ���ȫƽ����
        return True
    else:
        return False

def same(x):             # ���x���Ƿ�����λ��ͬ
    d1 = x%10            # x�ĸ�λ��
    d2 = (x/10)%10       # x��ʮλ��
    d3 = x/100           # x�İ�λ��
    if d1<>d2 and d2<>d3 and d1<>d3:
        return False
    else:
        return True
    
def main():
    n = getInput()
    count = 0
    for x in range(100,n+1):
        if perfect(x) and same(x):
            print x
            count = count + 1
    print "���ҵ�"+str(count)+"��������������ȫƽ����"

main()
            
