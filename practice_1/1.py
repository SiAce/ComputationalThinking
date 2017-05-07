#Purpose : Encrypt a four-digit number
#Author: SiAce
#Date: 3/10/2017

print "Enter a number:"
num = input()
a = [0,0,0,0]
b = [0,0,0,0] 
a[0] = num/1000
a[1] = (num % 1000) / 100
a[2] = (num % 100) /10
a[3] = num % 10 # Convert number into an array
for i in range(4):
    b[i] = (a[i] + 9) % 10 # Store the first result of encryption into b
print "The result of encryption is %s%s%s%s" %(b[2],b[3],b[0],b[1])

