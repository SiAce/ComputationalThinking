# -*- coding: cp936 -*-

# 输入两个正整数a和n
# 计算a + aa + aaa +...+ a...a（n个a）之和
# 例如：输入2和3，计算的是2+22+222，即246。

a,n = input("请输入两个正整数: ")
d = len(str(a))
a1 = a
s = a
for i in range(n-1):
    a1 = a1*(10**d) + a
    s = s + a1
print s
