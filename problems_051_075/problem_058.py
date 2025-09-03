'''
PE #58
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

--------

After some math, it can be seen that the following equations hold:
Numbers on top-right diagonal:
    4x^2 + 6x + 3
Numbers on top-left diagonal:
    4x^2 + 8x + 5
Numbers on bottom-left diagonal:
    4x^2 + 10x + 7

Found by starting at odd square (2x+1)^2 and adding one more than that to each
    starting. (13 = (2x+1)^2 + 2x + 2)
Other diagonals require another 2x+2 for each jump

---------

-generate list of numbers in each diagonal
-find number of primes in each
-compare against total number of numbers in lists

'''

def Diagonals(n): # creates list of numbers along diagonal
    topRight = [(2*x + 1)**2 + (2*x + 2)  for x in range(n)]
    topLeft = [(2*x + 1)**2 + 2*(2*x + 2)  for x in range(n)]
    bottomLeft = [(2*x + 1)**2 + 3*(2*x + 2)  for x in range(n)]
    return [1] + topRight + topLeft + bottomLeft

def PrimeCheck(x):
    if x == 1:
        return False
    if x % 2 == 0 and x != 2:
        return False
    for i in range(3, int(x**.5)+1, 2):
        if x % i == 0:
            return False
    return True

n = 1

while True:
    l = Diagonals(n)
    primes = [x for x in l if PrimeCheck(x)]
    if len(primes)/len(l) < .1:
        print("Diagonals:")
        print(l)
        print("Size of square:")
        print(2*n + 1)
        break
    n += 1
    
    
    