from helpers import *

lines = getlines(3)
total = 0

for line in lines:
	a, b = line[:len(line) // 2], line[len(line) // 2:]

	l = ord(list(set(a).intersection(set(b)))[0])
	
	if l >= ord("a"):
		total += 1 + (l - ord("a"))
	else:
		total += 27 + (l - ord("A"))

print(total)

total = 0
i = 0
while i < len(lines):
	group = lines[i:i+3]
	l = ord(list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0])
	
	if l >= ord("a"):
		total += 1 + (l - ord("a"))
	else:
		total += 27 + (l - ord("A"))

	i += 3
print(total)