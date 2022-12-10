"""
Advent of Code 2022, day 10 : Cathode-Ray Tube

Your communication device broke; MacGyver its screen to get in contact with the elfs.
"""

from aoc import solver
s = solver.Solver('10')

def parse(file):
    lines = []
    for line in file:
        sections = [section.strip() for section in line.split(" ")]
        command = sections[0]

        if command == "addx":
            lines.append([command, int(sections[1])])
        elif command == "noop":
            lines.append([command])
    
    return lines

def solve(commands):
    command_queue = []
    for e in commands:
        if e[0] == "noop": command_queue.append([0, 0])
        if e[0] == "addx": command_queue.append([1, e[1]])

    x = 1
    cycle = 0
    signals = []

    while len(command_queue) != 0:
        active_command = command_queue[0]

        cycle += 1
        if cycle % 40 == 20: signals.append(cycle*x)

        if active_command[0] == 0:
            command_queue = command_queue[1:]
            x += active_command[1]

        active_command[0] -= 1

    return sum(signals)


def solve2(commands):
    command_queue = []
    for e in commands:
        if e[0] == "noop": command_queue.append([0, 0])
        if e[0] == "addx": command_queue.append([1, e[1]])

    x = 1
    cycle = 0
    screen = [['.' for _ in range(40)] for _ in range(6)]
    li = 0
    pi = 0

    while len(command_queue) != 0:
        pi = cycle % 40

        sprite = range(x-1, x+2)
        if pi in sprite: screen[li][pi] = '#'

        command = command_queue[0]
        if command[0] == 0:
            x += command[1] # move sprite position
            command_queue = command_queue[1:]

        if cycle % 40 == 0 and cycle != 0: li += 1

        command[0] -= 1
        cycle += 1

    return "\n".join(["".join(line) for line in screen])

s.part1(parse, solve)
print()
s.part2(parse, solve2)
