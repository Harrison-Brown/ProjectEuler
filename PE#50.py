'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

METHOD:
find strings of primes
 - record beginning prime and # of primes
 - eg 11: 2

maybe make consecutive prime class?
 - includes list function to grab all primes


'''

def isPrime(x):
    if x % 2 == 0 and x > 2:
        return False
    for i in range(3, int(x**.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def primeList(MAX):
    primes = []
    for i in gen_primes():
        if i > MAX:
            break
        primes.append(i)
    return primes


def main(MAX):
    primes = primeList(MAX)
    consec = {}
    delta = 20
    start = 0
    while True:
        l = primes[start:start+delta]
        if isPrime(sum(l)) and sum(l) <= MAX:
            consec[sum(l)] = l
            delta += 1
            start = 0
        elif sum(l) > MAX:
            if start == 0:
                break
            else:
                delta += 1
                start = 0
        elif sum(l) <= MAX:
            start += 1
    return consec


d = main(1000000)
key = list(d.keys())[-1]
print('The prime number {} can be written as the sum of {} primes.\n{}'.format(key, len(d[key]), d[key]))

# ANSWER: 997651
