from helpers import *

lines = getlines(4)
total = 0
total2 = 0

pairs = []

for line in lines:
	a1,a2,b1,b2, = getparts(line, "-,", "iiii")
	if (b1 >= a1 and b2 <= a2) or (a1 >= b1 and a2 <= b2):
		total += 1

	if b2 >= a1 and b1 <= a2:
		total2 += 1

print(total)
print(total2)
