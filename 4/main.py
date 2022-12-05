from aoc import solver
s = solver.Solver('4')

def parser(file):
  return [line.split(",") for line in file.readlines()]

def solver(data, task = 1):
  ""
  s = 0
  for pair in data:
    first, second = pair

    f1, f2 = map(int, first.split("-"))
    s1, s2 = map(int, second.split('-'))

    ff = set(range(f1, f2+1))
    ss = set(range(s1, s2+1))

    if task == 1:
      if ff <= ss or ff >= ss: s += 1
    else:
      if ff & ss: s += 1

  return s

s.part1(parser, solver)
s.part2(parser, solver, 2)
