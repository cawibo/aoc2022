"""
Advent of Code 2022, day 11 : Monkey in the Middle

Some monkeys are throwing around your belongings.
"""
import copy
import functools

from aoc import solver
s = solver.Solver('11')

monkeys1 = [
    dict(
        items=[int(e) for e in [79, 98]],
        operation=lambda x: x * 19,
        test=lambda x: pow(x, 1, 23) == 0,
        true=2,
        false=3.
    ),
    dict(
        items=[int(e) for e in [54, 65, 75, 74]],
        operation=lambda x: x + 6,
        test=lambda x: pow(x, 1, 19) == 0,
        true=2,
        false=0
    ),
    dict(
        items=[int(e) for e in [79, 60, 97]],
        operation=lambda x: x * x,
        test=lambda x: pow(x, 1, 13) == 0,
        true=1,
        false=3
    ),
    dict(
        items=[int(e) for e in [74]],
        operation=lambda x: x + 3,
        test=lambda x: pow(x, 1, 17) == 0,
        true=0,
        false=1
    )
]

monkeys2 = [
    dict(
        items=[66, 79],
        operation=lambda x: x * 11,
        test=lambda x: pow(x, 1, 7) == 0,
        mod=7,
        true=6,
        false=7
    ),
    dict(
        items=[84, 94, 94, 81, 98, 75],
        operation=lambda x: x * 17,
        test=lambda x: pow(x, 1, 13) == 0,
        mod=13,
        true=5,
        false=2
    ),
    dict(
        items=[85, 79, 59, 64, 79, 95, 67],
        operation=lambda x: x + 8,
        test=lambda x: pow(x, 1, 5) == 0,
        mod=5,
        true=4,
        false=5
    ),
    dict(
        items=[70],
        operation=lambda x: x + 3,
        test=lambda x: pow(x, 1, 19) == 0,
        mod=19,
        true=6,
        false=0
    ),
    dict(
        items=[57, 69, 78, 78],
        operation=lambda x: x + 4,
        test=lambda x: pow(x, 1, 2) == 0,
        mod=2,
        true=0,
        false=3
    ),
    dict(
        items=[65, 92, 60, 74, 72],
        operation=lambda x: x + 7,
        test=lambda x: pow(x, 1, 11) == 0,
        mod=11,
        true=3,
        false=4
    ),
    dict(
        items=[77, 91, 91],
        operation=lambda x: x * x,
        test=lambda x: pow(x, 1, 17) == 0,
        mod=17,
        true=1,
        false=7
    ),
    dict(
        items=[76, 58, 57, 55, 67, 77, 54, 99],
        operation=lambda x: x + 6,
        test=lambda x: pow(x, 1, 3) == 0,
        mod=3,
        true=2,
        false=1)
]


def parse1(_): return copy.deepcopy(monkeys1)
def parse2(_): return copy.deepcopy(monkeys2)


def solve1(monkeys):
    inspections = [0 for _ in range(len(monkeys))]

    for _ in range(20):
        for mi, me in enumerate(monkeys):
            for item in me["items"]:
                worry = me["operation"](item) // 3

                target = int(me["true"] if me["test"](worry) else me["false"])
                monkeys[target]["items"] += [worry]

                inspections[mi] += 1

            me["items"] = []

    result = sorted(inspections)[-2:]
    print("result", result)
    return result[0] * result[1]


def solve2(monkeys):
    inspections = [0 for _ in range(len(monkeys))]
    product = functools.reduce(lambda acc, curr: acc * curr["mod"], monkeys, 1)

    for R in range(10000):
        for mi, me in enumerate(monkeys):
            for item in me["items"]:
                worry = me["operation"](item)

                worry %= product
                target = int(me["true"] if me["test"](worry) else me["false"])

                monkeys[target]["items"] += [worry]

                inspections[mi] += 1

            me["items"] = []

    result = sorted(inspections)[-2:]
    print("result", result)
    return result[0] * result[1]


s.part1(parse1, solve1)
print()
s.part2(parse2, solve2)
