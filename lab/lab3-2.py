# -*- coding: cp936 -*-

# ����һ�����ֲ�ȫ��ͬ����λ����Ȼ����С�������������
# ��������������ɵ��������ȥ��������������ɵ���С����
# �ٶ����õ��Ĳ��ظ���������������ֱ��������ٱ仯Ϊֹ��
# ����������̡�
# ���磺����422�����
# 422��224��198
# 981��189��792
# 972��279��693
# 963��369��594
# 954��459��495
# 954��459��495

# �Ƚϸ�ʮ��λ�������ֵĴ�С
def compare(d1,d10,d100):
    if d1 > d10:              # ��λ������ʮλ��
        if d1 > d100:         # ��λ�����ڰ�λ��
            maxD = d1         # ��λ�����
            if d10 > d100:    # ʮλ�����ڰ�λ��
                midD = d10    # ʮλ������
                minD = d100   # ��λ����С
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
    d1 = n%10                             # ��λ
    d10 = (n/10)%10                       # ʮλ
    d100 = (n/100)%10                     # ��λ
    maxD,midD,minD = compare(d1,d10,d100)  # ��λ�����ųɴ���С
       
    big = 100*maxD + 10*midD + minD       # ��ϳ������
    small = 100*minD + 10*midD + maxD     # ��ϳ���С��
    return big,small

def main():
    n = input("������һ����λ��Ȼ������λ����ȫͬ����")
    ok = False
    old = 0                  # ��¼��һ�εĲ�ֵ����ʼ��Ϊ0
    while not ok:  
        b,s = bigsmall(n)    # ���ţ���ϳ����������С��
        n = b - s            # ���������ȥ��С��
        print "%d - %d = %d" % (b,s,n)
        if n == old:         # ��ֵ���ٱ仯
            ok = True
        else:
            old = n
    print "�����˺ڶ���",old

main()
