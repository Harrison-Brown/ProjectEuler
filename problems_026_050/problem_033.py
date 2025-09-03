'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
class Q:
    def __init__(self, n, d = 1):
        self.n = n
        self.d = d
        self.reduce()

    def __add__(self, other):
        n = (self.n * other.d) + (self.d * other.n)
        d = self.d * other.d
        return Q(n, d)

    def __sub__(self, other):
        other.n = -other.n
        return self + other

    def __mul__(self, other):
        n = self.n * other.n
        d = self.d * other.d
        return Q(n, d)

    def __truediv__(self, other):
        other.n, other.d = other.d, other.n
        return self * other

    def reduce(self):
        a = max(self.n, self.d)
        b = min(self.n, self.d)
        while b:
            a, b = b, a % b
        a = abs(a)
        self.n = self.n // a
        self.d = self.d // a

    def __str__(self):
        if self.d == 1:
            return 'Q({})'.format(self.n)
        else:
            return 'Q({}, {})'.format(self.n, self.d)

    def __eq__(self, other):
        if self.n == other.n and self.d == other.d:
            return True
        else:
            return False

    def __repr__(self):
        return self.print()

    def print(self):
        if self.d == 1:
            return '{}'.format(self.n)
        else:
            return '{}/{}'.format(self.n, self.d)

results = []

qlist = [(n, d) for d in range(10, 100) for n in range(10, d)]

for pair in qlist:
    n, d = pair
    if not '0' in str(n):
        for a in str(n):
            if a in str(d):
                try:
                    n = int(str(n).replace(a, ''))
                    d = int(str(d).replace(a, ''))
                    if Q(*pair) == Q(n, d):
                        print(pair, Q(n, d))
                        results.append(Q(n, d))
                except:
                    pass

prod = Q(1)
for x in results:
    prod = prod * x

print(prod)

# ANSWER: 100
