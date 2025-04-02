"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
https://adventofcode.com/2015/day/3
"""
from aocd.models import Puzzle


p = Puzzle(day=3, year=2015)
input = p.input_data

dirs = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
loc = [0,0]
visited = set()
visited.add(tuple(loc))
for dir in input:
    loc[0] += dirs[dir][0]
    loc[1] += dirs[dir][1]
    visited.add(tuple(loc))

p.answer_a = len(visited)