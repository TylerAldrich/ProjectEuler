import sys
import math

def d(n):
    if n % 2 == 0:
        max = n/2
    else:
        max = (n-1)/2

    L = list()
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            L.append(i)
            if i != 1:
                L.append(n/i)
        i += 1

    total = 0
    for x in L:
        total += x

    return total

print "STARTING:"
amicable_numbers = list()
for i in range(1, 10000):
    if d(d(i)) == i and d(i) != d(d(i)):
        print i,
        amicable_numbers.append(i)
    if i % 1000 == 0:
        print ".",
        sys.stdout.flush()

print "   [DONE]"

amicable_numbers = list(set(amicable_numbers))

total = 0
for x in amicable_numbers:
    total += x

print total

print math.sqrt(220)
