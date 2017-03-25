n = input('n:')
index = ord('A')
for i in range(n):
    for j in range(n-i):
        print chr(index),
        index = index + 1
    print 
