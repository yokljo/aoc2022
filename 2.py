from helpers import *

lines = getlines(2)

winners = {
	"A": "Y",
	"B": "Z",
	"C": "X",
}

winners2 = {
	"A": "B",
	"B": "C",
	"C": "A",
}
losers2 = {
	"A": "C",
	"B": "A",
	"C": "B",
}

total = 0
total2 = 0

for line in lines:
	m, n = getparts(line, " ", "ss")
	mi = ord(m) - ord("A") + 1
	ni = ord(n) - ord("X") + 1
	score = ni
	if mi == ni:
		score += 3
	elif n == winners[m]:
		score += 6

	total += score

	score2 = 0
	if n == 'X':
		played = losers2[m]
	elif n == 'Y':
		played = m
		score2 += 3
	elif n == 'Z':
		played = winners2[m]
		score2 += 6
	score2 += ord(played) - ord("A") + 1
	total2 += score2

print(total, total2)
