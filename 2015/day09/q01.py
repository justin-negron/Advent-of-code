"""
--- Day 9: All in a Single Night ---
https://adventofcode.com/2015/day/9
"""
from aocd.models import Puzzle
from itertools import permutations

p = Puzzle(day=9, year=2015)
input = p.input_data.splitlines()

def find_shortest_path(distances, cities):
    shortest = float('inf')
    for route in permutations(cities):
        distance = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
        shortest = min(shortest, distance)
    return shortest

def parse_input(input):
    distances = {}
    cities = set()
    for line in input:
        city1, to, city2, eq, dist = line.split()
        dist = int(dist)
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}
        distances[city1][city2] = dist
        distances[city2][city1] = dist
        cities.update([city1, city2])
    return distances, cities

distances, cities = parse_input(input)
shortest = find_shortest_path(distances, cities)

p.answer_a = shortest