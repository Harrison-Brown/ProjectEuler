'''
PE#14
Longest Collatz sequence (under 1 million)
'''
most = 0
def sequence(a):
    count = 1
    while a >= 1:
        if a == 1:
            return count
        elif a % 2 == 0:
            a = a // 2
        else:
            a = (3 * a) + 1
        count = count + 1
           
for i in range(1, 1000000):
    n = sequence(i)
    if n > most:
        most = n
        print("%s has longest sequence of %s" % (i, most))
print("Done!")
input()
#ANSWER = 837799
