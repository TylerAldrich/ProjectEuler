
max_perim = 1000

def valid_triangle(a,b,c):
    return a**2 + b**2 == c**2

all_combo_list = []

for a in range(1, max_perim):
    for b in range(a, max_perim - a):
        for c in range(b, max_perim - a - b):
            combo = [a, b, c]
            combo.sort()
            if combo not in all_combo_list and valid_triangle(a, b, c):
                all_combo_list.append(combo)
                print combo

print "Created combo list"

# calculates number of integer solutions for a given perimeter
def integer_solutions(perim):
    solutions = 0

    for combo in all_combo_list:
        a, b, c = combo
        if a + b + c == perim:
            solutions += 1

    return solutions

solution_num = 0
perim = 0
for i in range(1, 1001):
   sols = integer_solutions(i)
   if sols > solution_num:
       solution_num = sols
       perim = i


print solution_num
print perim
