'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''


#p067_triangle.txt

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def main(t):
	for i in range(len(t), 0, -1):
		i -= 1 #fix index issues
		for x in t:
			print(x) #print out the triangle each step
		for j in range(0, len(t[i])-1): #-1 because we index 2 values at a time
			if t[i][j] > t[i][j+1]:
				t[i-1][j] += t[i][j]
			elif t[i][j] <= t[i][j+1]:
				t[i-1][j] += t[i][j+1]
		del t[i] #remove clutter in list

def StringToList(s):
	l = []
	for i in range(0, len(s), 3):
		n = int(s[0+i:2+i])
		l.append(n)
	return l
	


file = open("p067_triangle.txt", "r")
l = file.readlines()
t = []
for line in l:
	t.append(StringToList(line))
	
main(t)

#ANSWER: 7273