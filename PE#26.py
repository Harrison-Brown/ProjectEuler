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
    
    def print(self):
        if self.d == 1:
            return '{}'.format(self.n)
        else:
            return '{}/{}'.format(self.n, self.d)

Counts = [0, 0] # 0, 1, 2, ....

def CycleCount(x): # Where x is a fraction
    if x.d % 2 == 0 or x.d % 5 == 0:
        return 0
    n = 1
    while True:
        i = Q( (x.n * (10**n)) % x.d, x.d)
        if x == i:
            return n
        else:
            n += 1
        
for i in range(2, 1001):
    x = Q(1,i)
    Counts.append(CycleCount(x))

d = Counts.index(max(Counts))

print('{} has the longest digit cycle of {}'.format(d, Counts[d]))












