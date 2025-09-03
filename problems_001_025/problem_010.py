'''
PE#10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def check_prime(p):
    if p == 2:
        return True
    elif p % 2 == 0:
        return False
    for i in range(3, int(p**.5)+1, 2):
        if p % i == 0:
            return False
    return True


TestVar = 3 # skip number 2 to go up by odds
prime_total = 2 # since skipped 2, put it in total
while TestVar < 2000000:
    if check_prime(TestVar):
        prime_total = prime_total + TestVar
    TestVar = TestVar + 2
print("The sum of primes under 2,000,000 is {}".format(prime_total))
#ANSWER = 142913828922
