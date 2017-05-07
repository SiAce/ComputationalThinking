a = input('a:')
n = input('n:')
sum = 0
for i in range(n):
    term = 0
    for j in range(i+1):
        term += a*10**j
    sum += term

print sum
