from aoc import solver
s = solver.Solver('6')

def parse(file):
  return file.read().strip()

def solve(data, packet_size):
  
  for index in range(packet_size, len(data)):
    ss = set([e for e in data[index - packet_size : index]])

    if (len(ss)) == packet_size: return index

s.part1(parse, solve, 4)
print()
s.part2(parse, solve, 14)
