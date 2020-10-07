'''
PE#24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import itertools

def concat(numList):
    s = ''.join(map(str, numList))
    return int(s)

p = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
numbers = []
for i in p:
    numbers.append(concat(i))

numbers.sort()
print("Answer: {}".format(numbers[1000000-1]))

# Answer: 