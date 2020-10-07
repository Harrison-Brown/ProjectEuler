# >>> d = {(2, 3): 4, (2, 5): 2}
# >>> max(d, key=d.get)
# (2, 3)
#####
#
# Program layout:
# 1) Generate values a, b
# 2) Test x values into function x^2 + ax + b
# 3) Determine if given x value yields prime
#   - If so, add 1 to counter, continue iterating
#   - If not, stop iterating, return length of consecutive primes
#
# Notes:
# b cannot be composite?
#####


import time
start = time.time()

def CheckPrime(x):
    if x < 2:
        return False
    for j in range(3, int(x**.5)+1, 2):
        if x % j == 0:
            return False
    return True

def CheckFunction(a, b): # returns # of consecutive integers of primes
    x = 0
    while True:
        p = x**2 + a*x + b
        if CheckPrime(p):
            x += 1
        else:
            return x

QuadraticPrimes = {} # Values stored in form (a, b): length
print('Testing (a, b)...')

for a in range(-999, 1000):
    for b in range(-999, 1001, 2):
        n = CheckFunction(a, b)
        QuadraticPrimes[(a, b)] = n

MaxA, MaxB = max(QuadraticPrimes, key = QuadraticPrimes.get)

print('The longest list of consecutive primes is {} from a = {} and b = {}'.format(QuadraticPrimes[(MaxA, MaxB)], MaxA, MaxB))


stop = time.time()
print('Time elapsed: {} seconds'.format(stop - start))
    
