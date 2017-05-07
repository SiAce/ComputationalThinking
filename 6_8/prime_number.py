number_list = []
n = input("Please input a number greater than 1: ")

for i in range(2, n+1):
    number_list.append(i)

print "Prime numbers between 2 and %d are:" %n,

while len(number_list) > 0 :

    prime_number = number_list[0]
    length = len(number_list)

    print prime_number,

    for i in range(1, number_list[length - 1]/prime_number + 1):
        try:
            number_list.remove(prime_number*i)
        except:
            continue
