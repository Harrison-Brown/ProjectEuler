'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def check_prime(p):
    j = 3
    while j < int(p ** 0.5):
        if p % j == 0:
            return False
        else:
            j = j + 2
    return True
n = 600851475143
i = int(n ** 0.5) - 1
while i > 0:
    if n % i == 0:
        print (str(i) + ' divides ' + str(n))
        if check_prime(i):
            print (str(i) + ' is prime!')
            input()
    i = i - 2
        
#ANSWER = 6857
