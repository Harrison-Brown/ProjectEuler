'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def get_digit(n, p):
    place = 10 ** p
    digit = int((n // place)) % 10
    return digit
	
n = 2 ** 1000
p = 0
sum = 0
print(n)

while True:
	d = get_digit(n, p)
	sum = d + sum
	p = p + 1
	print(sum)

input()

#ANSWER = 1366