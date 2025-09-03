'''
PE#21
Amicable Numbers
d(n) is the sum of proper divisors of n.
if d(a)=b and d(b)=a then a and b are an amicable pair
find the sum of amicable numbers under 10000

pick number a
find sum of factors b
if sum of factors of b is a
	include a, b
		check if a, b is in list

'''
from time import clock # for counting how long a program takes
start = clock()

pairs = []

def d(n):
	factors = [1]
	for i in range(2, int(n**.5)+1):
		if n % i == 0:
			factors.append(i)
			factors.append(n//i)
	if (n**.5) % 1 == 0:
		factors.append(int(n**.5))
	return int(sum(factors))
	
for a in range (5, 10001): #need to include 10000
	b = d(a)
	c = d(b)
	if c == a and a != b and pairs.count(a) == 0:
		pairs.append(a)
		pairs.append(b)

print("Time taken:", round(clock() - start,5), "seconds")
print(sum(pairs))
input()

#ANSWER = 31626