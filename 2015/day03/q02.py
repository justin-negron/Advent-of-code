"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
https://adventofcode.com/2015/day/3
"""
from aocd.models import Puzzle


p = Puzzle(day=3, year=2015)
input = p.input_data

dirs = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
santa_loc = [0,0]
robos_loc = [0,0]
visited = set()
visited.add(tuple(santa_loc))
for i, dir in enumerate(input):
    if i % 2 == 0:
        santa_loc[0] += dirs[dir][0]
        santa_loc[1] += dirs[dir][1]
        visited.add(tuple(santa_loc))
    else:
        robos_loc[0] += dirs[dir][0]
        robos_loc[1] += dirs[dir][1]
        visited.add(tuple(robos_loc))

p.answer_b = len(visited)