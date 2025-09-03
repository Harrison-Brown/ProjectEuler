'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

prime_file = open("primes.txt", "r")
primes = []
string = prime_file.read()
for x in string.split(", "):
	if x == '':
		break
	primes.append(int(x))

def isCircular(x):
    s = str(x)
    for i in s:
        s = s[1:] + s[0]
        if int(s) not in primes:
            return False
    return True

primes = [x for x in primes if x < 1000000] #limit to only 1,000,000 primes

circulars = []


for x in primes:
    if isCircular(x):
        print(x)
        circulars.append(x)

#ANSWER: 55