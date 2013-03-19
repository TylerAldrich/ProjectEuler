
table = {}

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n in table:
        return table[n]
    else:
        table[n] = fib(n-1) + fib(n-2)
        return table[n]

def num_digits(n):
    count = 0

    while n >= 1:
        n /= 10
        count += 1

    return count

i = 1
while num_digits(fib(i)) < 1000:
    i += 1

print i

