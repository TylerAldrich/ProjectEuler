import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

times = 100000

total_indices = 0

for i in xrange(times):
    random.shuffle(numbers)

    total_indices += (numbers.index(6) + 1)
    numbers = [1,2,3,4,5,6,7,8,9,10]

print "Times ran:" + str(times)
print float(total_indices) / times





