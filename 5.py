from copy import deepcopy
from helpers import *

lines = getlines(5)
total = 0

breakIndex = lines.index("")
origStacks = [[c for c in stack[::-1] if c != " "] for stack in zip(*(line[1::4] for line in lines[:breakIndex-1]))]

def run(part2):
	stacks = deepcopy(origStacks)
	for line in lines[breakIndex+1:]:
		_, nToMove, _, fromInd, _, toInd = getparts(line, " ", "sisisi")
		top = stacks[fromInd-1][-nToMove:]
		stacks[toInd-1] += stacks[fromInd-1][-nToMove:][::1 if part2 else -1]
		stacks[fromInd-1] = stacks[fromInd-1][:-nToMove]

	print("".join([s[-1] for s in stacks if len(s) > 0]))

run(False)
run(True)