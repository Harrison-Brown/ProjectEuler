'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
from time import clock
start = clock()
list = []

for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				for e in range(10):	
					for f in range(10):
						str = "%s%s%s%s%s%s" % (a, b, c, d, e, f)
						n = int(str)
						if n == (a**5) + (b**5) + (c**5) + (d**5) + (e**5) + (f**5):
							list.append(n)
							print(list, sum(list))
						
print(sum(list))
print("Time taken:", round(clock() - start,5), "seconds")
input()

#ANSWER = 443839