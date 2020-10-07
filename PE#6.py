'''
PE#6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_squares():
    total = 0
    for i in range(1, 101):
        total = total + (i ** 2)
    print ("sum of squares is %s" % (total))
    return total

def square_of_sum():
    total = 0
    for i in range(1, 101):
        total = total + i
        print (str(total))
    total = total ** 2
    print ("square of sum is %s" % (total))
    return (total)

x = square_of_sum() - sum_of_squares()
print (str(x))

#ANSWER = 25164150
