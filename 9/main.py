"""
Advent of Code 2022, day 9 : Rope Bridge

The elfs are crossing a rope bridge.
"""
import math
from aoc import solver
s = solver.Solver(9)

def parse(file):
    pairs = [line.split(" ") for line in file.readlines()]
    return [(moves[pair[0]], int(pair[1])) for pair in pairs]

moves = {
    "R": complex(1,0),
    "L": complex(-1, 0),
    "U": complex(0, 1),
    "D": complex(0, -1)
    }

def solve(lines, sections = 10):
    snake = [complex(0, 0) for _ in range(sections)]
    visited = set()

    visited.add(snake[-1])

    for move, n in lines:
        for _ in range(n):
            snake[0] += move

            for i in range(1, sections):
                difference = snake[i-1] - snake[i]

                if abs(difference) < 2: continue

                diff_x = difference.real and math.copysign(1, difference.real)
                diff_y = difference.imag and math.copysign(1, difference.imag)

                snake[i] += complex(diff_x, diff_y)
            visited.add(snake[-1])

    return len(set(visited))

s.part1(parse, solve, 2)
print()
s.part2(parse, solve, 10)
