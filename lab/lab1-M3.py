# -*- coding: cp936 -*-

# 输入正整数n，输出
# 2/1 + 3/2 + 5/3 + 8/5 + ...
# 的前n项之和.
#（后项分子是前项分子分母之和，后项分母是前项分子）

def main():
    n = input("请输入求和项数n：")
    a,b = 2,1
    s = 1.0*a/b
    for i in range(n-1):
        s = s + 1.0*(a+b)/a
        a,b = a+b,a
    print "前n项之和为：",s

main()
