from aoc import solver
s = solver.Solver('3')

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
mapping = dict([c, i+1] for i, c in enumerate(letters))

def parse1(file):
  data = []

  for line in file.read().split("\n"):
    m = len(line) // 2
    data += [[line[:m], line[m:]]]

  return data

def parse2(file):
  data = []

  lines = file.read().split("\n")

  for index in range(0, len(lines), 3):
    line1 = lines[index]
    line2 = lines[index+1]
    line3 = lines[index+2]

    data += [[line1, line2, line3]]

  return data

def solve1(lines):
  score = 0

  for left, right in lines:
    ls = set([c for c in left])

    for c in right:
      if c in ls:
        score += mapping[c]
        break

  return score

def solve2(data):
  score = 0

  for l1, l2, l3 in data:
    s1 = set([e for e in l1])
    s2 = set([e for e in l2])
    s3 = set([e for e in l3])
    
    s = s1 & s2 & s3

    score += mapping[list(s)[0]]

  return score

s.part1(parse1, solve1)
print()
s.part2(parse2, solve2)