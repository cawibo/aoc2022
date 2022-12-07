"""
Advent of Code 2022, day 7 : No Space Left On Device

The elfs' communication device requires a system update, but there is no space left.
"""

from aoc import solver
s = solver.Solver('7')


def parse(file):
    """returns a file structure"""

    def resolve():
        """returns current directory node"""
        node = root
        for step in path:
            node = node[step]
        return node

    history = [line.strip().split("\n")
               for line in file.read().split("$ ")][2:]

    root = {'': {}}
    path = ['']
    current = None

    for command, *output in history:
        if command == 'ls':
            current = resolve()

            for line in output:
                if line[:3] == 'dir':
                    # initialize directory
                    _, name = line.split(' ')
                    current[name] = {}

                else:
                    # store file
                    size, name = line.split(' ')
                    current[name] = int(size)

        if command[:2] == 'cd':
            _, step = command.split(' ')

            if step == '/':
                # reset path
                path = ['']
            elif step == '..':
                # step out of
                path = path[:-1]
            else:
                # step into
                path += [step]

    return root


def getSizes(d):
    """returns an array of all directory sizes"""
    sizes = []
    this = 0
    for _, val in d.items():
        if type(val) == dict:
            result = getSizes(val)
            this += result[0]
            sizes += result
        else:
            this += val
    return [this] + sizes


def solve1(root):
    """returns the sum of all directory sizes <= 1e5"""
    return sum([e for e in getSizes(root['']) if e <= 100000])


def solve2(root):
    """returns the size of the smallest directory that can be removed to make sufficient room for the update"""
    sizes = [e for e in getSizes(root[''])]
    def isSufficient(size): return 4e7 - sizes[0] + size >= 0

    return next(filter(isSufficient, sorted(sizes[1:])), None)


s.part1(parse, solve1)
print()
s.part2(parse, solve2)
