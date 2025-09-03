'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

--------
Loop:
1- Start with prime 2, 3, 5, 7
2- Truncate number to the right (avoid 2, 4, 5, 6, 8, 0, not prime)
3- Check if truncated number N is prime
4- If so, add N to list
5- Go to 2, try another truncate



'''

rightPrimes = [2, 3, 5, 7] # adding digits to the right
leftPrimes = [1, 3, 5, 7] # adding digits to the left



def PrimeCheck(x):
    if (x % 2 == 0 and x != 2) or x == 1:
        return False
    for i in range(3, int(x**.5)+1, 2):
        if x % i == 0:
            return False
    return True


def rightAppend(l):
    for p in l:
        for i in [1, 3, 7, 9]:
            x = 10*p + i
            if PrimeCheck(x):
                l.append(x)
    return l

def leftAppend(l):
    for p in l:
        for i in [1, 3, 7, 9]:
            x = int(str(i) + str(p))
            if PrimeCheck(x):
                l.append(x)
    return l
            

rightAppend(rightPrimes)
leftAppend(leftPrimes)
TruncatablePrimes = [x for x in leftPrimes if x in rightPrimes and x > 10]
print(TruncatablePrimes)
print(sum(TruncatablePrimes))