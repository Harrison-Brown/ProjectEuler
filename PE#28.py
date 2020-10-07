'''
PE#28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''
from time import clock
start = clock()
sum = 1

for n in range(2, 502): 
	sum = sum + (((2*n)-1)**2) #up-right diagonal
	sum = sum + (((2*n)-1)**2) - (6 * (n-1)) #down-right diagonal
	sum = sum + ((2*n - 2)**2 + 1) #down-left diagonal
	sum = sum + (((2*n)-1)**2) - (2 * (n-1)) #up-left diagonal
	
print(sum)
print("Time elapsed: ", round(clock() - start, 5))
input()

#ANSWER = 669171001