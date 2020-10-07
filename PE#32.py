'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def Factors(x): #Finds set of factors, returns set
    factors = set() #sets don't store same value twice, unordered
    for i in range(1, int(x**.5) + 1):
        if x % i == 0:
            factors.add(i)
            factors.add(int(x/i))
    return factors

def hasRepeats(n): # Check if n itself has any number repeats;
    l = [i for i in str(n)] 
    if len(l) != len(set(l)):
        return True 
    else:
        return False

def isPandigital(n):
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    if hasRepeats(n): # First check
        return False
    factors = list(Factors(n))
    for i in factors:
        a, b = i, n // i # // finds integer quotient
        #factors.remove(a)
        #factors.remove(b)
        #print(a, b)
        s = str(a) + str(b) + str(n)
        number = {int(i) for i in s}
        if digits == number:
            return True

Pandigital_Products = [x for x in range(1000, 10000) if isPandigital(x)]
# Doesn't go above 10000-ish, will use too many numbers

print(Pandigital_Products)
print(sum(Pandigital_Products))

# Answer: 45228

    
    
    

