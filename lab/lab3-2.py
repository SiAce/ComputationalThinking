# -*- coding: cp936 -*-

# 输入一个数字不全相同的三位数，然后进行“重排求差”操作：
# 用这三个数字组成的最大数减去用这三个数字组成的最小数。
# 再对所得到的差重复“重排求差”操作，直至“差”不再变化为止。
# 输出操作过程。
# 例如：输入422，输出
# 422－224＝198
# 981－189＝792
# 972－279＝693
# 963－369＝594
# 954－459＝495
# 954－459＝495

# 比较个十百位三个数字的大小
def compare(d1,d10,d100):
    if d1 > d10:              # 个位数大于十位数
        if d1 > d100:         # 个位数大于百位数
            maxD = d1         # 个位数最大
            if d10 > d100:    # 十位数大于百位数
                midD = d10    # 十位数居中
                minD = d100   # 百位数最小
            else:
                midD = d100
                minD = d10
        else:
            maxD = d100
            midD = d1
            minD = d10
    else:
        if d10 > d100:
            maxD = d10
            if d1 > d100:
                midD = d1
                minD = d100
            else:
                midD = d100
                minD = d1
        else:
            maxD = d100
            midD = d10
            minD = d1
    return maxD,midD,minD
    
def bigsmall(n):
    d1 = n%10                             # 个位
    d10 = (n/10)%10                       # 十位
    d100 = (n/100)%10                     # 百位
    maxD,midD,minD = compare(d1,d10,d100)  # 三位数字排成大中小
       
    big = 100*maxD + 10*midD + minD       # 组合成最大数
    small = 100*minD + 10*midD + maxD     # 组合成最小数
    return big,small

def main():
    n = input("请输入一个三位自然数（各位不能全同）：")
    ok = False
    old = 0                  # 记录上一次的差值，初始化为0
    while not ok:  
        b,s = bigsmall(n)    # 重排：组合成最大数和最小数
        n = b - s            # 求差：最大数减去最小数
        print "%d - %d = %d" % (b,s,n)
        if n == old:         # 差值不再变化
            ok = True
        else:
            old = n
    print "发现了黑洞：",old

main()
