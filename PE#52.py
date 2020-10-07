'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def main(n):
        l = [ sorted([int(x) for x in str(n * i)]) for i in range(1, 7) ]
        for a in l:
            if a != sorted([int(x) for x in str(n)]):
                return False
        return True

n = 1
while True:
    if main(n):
        print('found!', n)
        break
    n += 1

# ANSWER: 142857
