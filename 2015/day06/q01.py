"""
--- Day 6: Probably a Fire Hazard ---
https://adventofcode.com/2015/day/6
"""
from aocd.models import Puzzle


p = Puzzle(day=6, year=2015)
input = p.input_data.splitlines()

power = {'on': 1, 'off': 0}
grid = [[0 for _ in range(1000)] for _ in range(1000)]

def toggle(start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            grid[i][j] ^= 1

def onoff(start, end, instr):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            grid[i][j] = power[instr]

for line in input:
    instr = line.split(" ")

    # toggle
    if(len(instr) == 4):
        start = [int(x) for x in instr[1].split(',')]
        end = [int(x) for x in instr[3].split(',')]
        toggle(start, end)
    # turn on/off
    else:
        start = [int(x) for x in instr[2].split(',')]
        end = [int(x) for x in instr[4].split(',')]
        onoff(start, end, instr[1])

p.answer_a = sum(row.count(1) for row in grid)