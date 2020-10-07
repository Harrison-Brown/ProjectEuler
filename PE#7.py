'''
PE#7
Harrison Brown 

What is the 10 001st prime number?
'''
primes = [2, 3, 5, 7]

def check_prime(n): # Rather than check all numbers, just check current primes
    global primes
    for i in primes: 
        if n % i == 0: # If n is divisible by any prime, its not prime
            return False
        if i > n**.5: 
            break
    return True

n = 9 # next number to check in primes, odd.
while len(primes) < 10001:
    if check_prime(n):
        primes.append(n)
    n += 2 # count by 2s, skip evens.
        
print("Answer: {}".format(primes[-1]))


# ANSWER = 104527