# -*- coding: cp936 -*-

# ��������������a��n
# ����a + aa + aaa +...+ a...a��n��a��֮��
# ���磺����2��3���������2+22+222����246��

a,n = input("����������������: ")
d = len(str(a))
a1 = a
s = a
for i in range(n-1):
    a1 = a1*(10**d) + a
    s = s + a1
print s
