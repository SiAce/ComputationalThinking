# -*- coding: cp936 -*-

print '[1]ƻ��'
print '[2]��'
print '[3]����'
print '[4]����'
print '[0]�˳�'

for i in range(4):
    number = input('��������ţ�')
    if number == 1 :
        print 'ƻ����3.00'
    elif number == 2:
        print '�棺2.50'
    elif number == 3:
        print '���ӣ�4.10'
    elif number == 4:
        print '���ѣ�10.20'
    elif number == 0:
        break
    else:
        print '��������Ч�����֣�'
    
