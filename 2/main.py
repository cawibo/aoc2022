from aoc import solver
s = solver.Solver('2')

def parse(file):
  return [[mapping[e] for e in line.split()] for line in file.readlines()]

mapping = {
  "A": 0,
  "B": 1,
  "C": 2,
  "X": 0,
  "Y": 1,
  "Z": 2
}

def solve1(lines):
  score = 0

  for theirs, mine in lines:

    if mine == (theirs + 1) % 3:
      score += 6 + mine
    elif mine == theirs:
      score += 3 + mine
    else:
      score += mine

    score += 1 # to account for the -1 mapping

  return score

def solve2(lines):
  score = 0

  for theirs, outcome in lines:

    if outcome == 0:
      score += (theirs - 1) % 3
    elif outcome == 1:
      score += theirs + 3
    else:
      score += (theirs + 1) % 3 + 6

    score += 1 # to account for the -1 mapping

  return score

s.part1(parse, solve1)
print()
s.part2(parse, solve2)