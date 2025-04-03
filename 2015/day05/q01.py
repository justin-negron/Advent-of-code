"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
https://adventofcode.com/2015/day/5
"""
from aocd.models import Puzzle


p = Puzzle(day=5, year=2015)
input = p.input_data.splitlines()

vowels = {'a', 'e', 'i', 'o', 'u'}
not_allowed = {"ab", "cd", "pq", "xy"}

total_nice_strings = 0

for line in input:
    is_nice_string = True
    has_double = False
    total_vowels = 0
    for i in range(len(line) - 1):
        if line[i:i+2] in not_allowed:
            is_nice_string = False
            break
        if line[i] == line[i+1]:
            has_double = True
        if line[i] in vowels:
            total_vowels += 1
        if i == len(line) - 2 and line[i+1] in vowels:
                total_vowels += 1

    if is_nice_string and has_double and total_vowels >= 3:
        total_nice_strings += 1

p.answer_a = total_nice_strings
