from aoc import solver
s = solver.Solver('1')

def parse(file):
  return [[int(e) for e in chunk.split('\n')] for chunk in file.read().split('\n\n')]

def solve(chunks, top = 1):
  return sum(sorted([sum(chunk) for chunk in chunks], reverse=True)[:top])

s.part1(parse, solve)
print()
s.part2(parse, solve, 3)