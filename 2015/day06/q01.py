"""
--- Day 6: Probably a Fire Hazard ---
https://adventofcode.com/2015/day/6
"""
from aocd.models import Puzzle


p = Puzzle(day=6, year=2015)
input = p.input_data.splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

def toggle(start, end):
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            grid[i][j] ^= 1

def on(start, end):
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            grid[i][j] = 1

def off(start, end):
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            grid[i][j] = 0

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
        if instr[1] == "on":
            print(start, end)
            on(start, end)
        elif instr[1] == "off":
            off(start, end)

# print(sum(row.count(1) for row in grid))
p.answer_a = sum(row.count(1) for row in grid)