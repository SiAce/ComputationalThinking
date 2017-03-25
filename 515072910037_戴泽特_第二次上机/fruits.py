# -*- coding: cp936 -*-

print '[1]苹果'
print '[2]梨'
print '[3]橘子'
print '[4]葡萄'
print '[0]退出'

for i in range(4):
    number = input('请输入序号：')
    if number == 1 :
        print '苹果：3.00'
    elif number == 2:
        print '梨：2.50'
    elif number == 3:
        print '橘子：4.10'
    elif number == 4:
        print '葡萄：10.20'
    elif number == 0:
        break
    else:
        print '请输入有效的数字！'
    
