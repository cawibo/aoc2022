from aoc import solver
s = solver.Solver('5')

def parse(file):
  ""
  state, moves = file.read().split("\n\n")
  state = [[e for e in line[1::4]] for line in state.split('\n')]
  
  ns = [[] for _ in range(len(state[-1]))]
  state = state[:-1]

  for line in state[::-1]:
    for index, value in enumerate(line):
      if value != ' ':
        ns[index] += value

  ns = [stack[::-1] for stack in ns]

  moves = moves.split("\n")
  moves = [m.split(" ") for m in moves]
  moves = [(int(m[1]), int(m[3])-1, int(m[5])-1) for m in moves]

  return [ns, moves]

def solve(data, ordering):
  ""
  state, moves = data

  for n, frm, to in moves:
    frm_bef = [e for e in state[frm]]
    to_bef = [e for e in state[to]]

    tmp = state[frm][:n]
    state[frm] = state[frm][n:]
    state[to] = tmp[::ordering] + state[to]
    
    assert len(tmp) == n
    assert len(frm_bef) + len(to_bef) == len(state[frm]) + len(state[to])

  return "".join([e[0] for e in [e for e in state if len(e) > 0]])

s.part1(parse, solve, -1)
print()
s.part2(parse, solve, 1)