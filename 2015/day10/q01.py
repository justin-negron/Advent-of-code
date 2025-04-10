"""
--- Day 10: Elves Look, Elves Say ---
https://adventofcode.com/2015/day/10
"""
from aocd.models import Puzzle


p = Puzzle(day=10, year=2015)
input = p.input_data

def next_sequence(input):
    if len(input) == 1:
        return "".join(["1",input])
    sequence = ""
    prev = input[0]
    dupe = 1
    for num in input[1:]:
        if num == prev:
            dupe += 1
        else:
            sequence += "".join([str(dupe),str(prev)])
            dupe = 1
        prev = num
    sequence += "".join([str(dupe),str(prev)])
    return sequence

# perform sequence on input 40 times
for i in range(40):
    input = next_sequence(input)

# answer = length of result
p.answer_a = len(input)