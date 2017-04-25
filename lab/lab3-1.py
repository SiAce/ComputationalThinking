# -*- coding: cp936 -*-

# 输入一个三位数n，找出100～n之间所有满足如下条件的数x：
# x是完全平方数并且x有两位数字相同，如144，676等。
# 输出这样的x，并统计个数。

from math import sqrt

def getInput():
    n = input("请输入一个三位数：")
    while n<100 or n>999:
        print "输入有误"
        n = input("请输入一个三位数：")
    return n

def perfect(x):
    i = int(sqrt(x))     # 求x的平方根并取整
    if i**2 == x:        # 验证x是否完全平方数
        return True
    else:
        return False

def same(x):             # 检查x中是否有两位相同
    d1 = x%10            # x的个位数
    d2 = (x/10)%10       # x的十位数
    d3 = x/100           # x的百位数
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
    print "共找到"+str(count)+"个满足条件的完全平方数"

main()
            
