'''
PE#12
triangle numbers
'''
t = 10 #triangle number t
x = 4  #indexed by x
most_factors = 0
def factor_check(a):
    factors = 0
    for i in range(1, int(a**.5)):
        if a % i == 0:
            factors = factors + 2
    if (a ** .5) % 1 == 0:
        factors = factors + 1
    return factors
        
while True:
    x = x + 1
    t = t + x
    n = factor_check(t)
    if n > most_factors:
        most_factors = n
        print("%s has the most factors: %s" % (t, most_factors))
    if n > 500:
        print("Triangle number %s has %s factors!" % (t, n))
        input()

#ANSWER = 76576500
