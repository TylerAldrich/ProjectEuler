
def next_collatz(num):
    if num % 2 == 0:
        return num / 2
    else:
        return (3 * num) + 1

table = {}

def collatz(num):
    if num in table:
        return 1 + table[num]
    elif num == 1:
        return 1
    else:
        table[num] = 1 + collatz(next_collatz(num))
        return table[num]


biggest = 0
for i in range(1, 1000000):
    collatz_number = collatz(i)
    if collatz_number > biggest:
        biggest = collatz_number
        print i,
    print "\r",

print "\n^ Number that produces biggest collatz seq. under 1,000,000"
print "Longest sequece length = " + str(biggest)
