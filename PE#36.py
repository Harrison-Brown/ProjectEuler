'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def isPalindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def PalinGen():
    n = 1
    while True:
        b = bin(n)[2:]
        if isPalindrome(n) and isPalindrome(b):
            yield n
        n += 1

s = 0
for p in PalinGen():
    if p < 1000000:
        s += p
    else:
        break

print(s)

# ANSWER: 872187
