'''
PE#4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
largest = 0

def check_pal(n):
	for a in range(0, (len(str(n))//2)):
		if str(n)[a] != str(n)[len(str(n)) - a - 1]:
			return False
	return True
		

for a in range(100, 999):
	for b in range(100, 999):
		c = a * b
		if check_pal(c) and c > largest:
			largest = c
			print(largest, a, b)
print(largest, "Done!")
input()
