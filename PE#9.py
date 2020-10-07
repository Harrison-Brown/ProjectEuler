'''
PE#9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

#b^2 = (c^2 - a^2)

#start number = 500^.5

for c in range(500, 1, -1):    #possible c values
    for a in range(1, c - 1):  #possible a values given c
        b = ((c ** 2) - (a ** 2)) ** 0.5
        if b % 1 == 0 and (a + b + c) == 1000:
            print("found triplet: %s, %s, %s," % (a, b, c))
            print(str(a*b*c))

print("end")
#ANSWER=31875000
