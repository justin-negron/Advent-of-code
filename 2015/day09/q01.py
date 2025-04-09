"""
--- Day 9: All in a Single Night ---
https://adventofcode.com/2015/day/9
"""
from aocd.models import Puzzle
import sys


p = Puzzle(day=9, year=2015)
input = p.input_data.splitlines()

input = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()

paths = dict()
visit = set()
seen = set()

for line in input:
    line = line.split(" ")
    depart = line[0]
    dest = line[2]
    dist = line[4]
    paths[depart] = (dest, int(dist))
    visit.update([depart, dest])

shortest = sys.maxsize

for place in visit:
    if place in paths:
        sum = paths[place][1]
        check = place
        while check in paths:
            check, dist = paths[check]
            sum += dist
        
        shortest = min(shortest, sum)
    seen.add(place)



# p.answer_a = 