from helpers import *

lines = getlines(1)
total = 0

curr = []
elves = [curr]

for line in lines:
	if line == "":
		curr = []
		elves.append(curr)
	else:
		curr.append(int(line))

totals = [sum(c) for c in elves]

print(max(totals))

totals.sort()
print(sum(totals[-3:]))
