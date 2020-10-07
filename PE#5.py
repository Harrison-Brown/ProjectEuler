'''
PE#5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
n = 2520

def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""
   while(y):
       x, y = y, x % y
   return x

def lcm(x,y):
    lcm  = (x * y)/gcd(x,y)
    return lcm

n = 1
for i in range(2, 20):
    n = lcm(n, i)
    print (n)

#ANSWER = 232792560
