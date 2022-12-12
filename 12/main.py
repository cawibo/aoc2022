"""
Advent of Code 2022, day 12 : Hill Climbing Algorithm

You're climbing a mountain to increase signal strength.
"""

from queue import Queue
from aoc import solver
s = solver.Solver('12')


letters = "abcdefghijklmnopqrstuvwxyz"

mapping = dict(zip(letters, range(1, len(letters) + 1)))
mapping["S"] = 1
mapping["E"] = len(letters) + 1

UP = complex(-1, 0)
DOWN = complex(1, 0)
LEFT = complex(0, -1)
RIGHT = complex(0, 1)


def dijkstra(coords, start):
    cost = dict([[coord, 1e10] for coord in coords.keys()])
    cost[start] = 0

    neighbours = dict([[coord, None] for coord in coords.keys()])
    visited = set([start])

    queue = Queue(1e5)
    queue.put(start)

    while not queue.empty():
        U = queue.get()

        for direction in [UP, DOWN, LEFT, RIGHT]:
            node = direction + U

            if node in visited:
                continue
            if node not in coords:
                continue
            if coords[node] > coords[U] + 1:
                continue

            tmp_cost = cost[U] + 1
            if tmp_cost < cost[node]:
                cost[node] = tmp_cost
                neighbours[node] = U

            visited.add(node)
            queue.put(node)

    return cost


def parse(file, can_start_at_a=False):
    start = []
    end = None
    coords = dict()

    grid = [[c for c in line.strip()] for line in file.readlines()]

    for R in range(len(grid)):
        for C in range(len(grid[0])):
            cell = grid[R][C]
            coord = complex(R, C)

            coords[coord] = mapping[cell]

            if can_start_at_a and cell == "a":
                start.append(coord)
            if cell == "S":
                start.append(coord)
            if cell == "E":
                end = coord

    return [start, end, coords]


def parse2(file): return parse(file, can_start_at_a=True)


def solve(params):
    start, end, coords = params

    d = dijkstra(coords, start[0])

    return d[end]


def solve2(params):
    starts, end, coords = params

    low = 1e3
    for start in starts:
        d = dijkstra(coords, start)
        if low > d[end]:
            low = d[end]

    return low


s.part1(parse, solve)
print()
s.part2(parse2, solve2)
