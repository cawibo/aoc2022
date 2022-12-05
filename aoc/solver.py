class Solver:
  problemId = None

  def __init__(self, problemId):
    self.problemId = problemId

  def path(self, file_name):
    return f"{self.problemId}/{file_name}"

  def read_ex1(self, parse):
    with open(self.path('ex1'), 'r') as file:
      content = parse(file)
      return content

  def read_ex2(self, parse):
    with open(self.path('ex2'), 'r') as file:
      try:
        content = parse(file)
        if not content: raise
        return content
      except:
        return self.read_ex1(parse)

  def read_1(self, parse):
    with open(self.path('1'), 'r') as file:
      return parse(file)

  def read_2(self, parse):
    with open(self.path('2'), 'r') as file:
      try:
        content = parse(file)
        if not content: raise
        return content
      except:
        return self.read_1(parse)

  def part1(self, parser, solver, *args):
    print("part 1")
    
    example_data = self.read_ex1(parser)
    print(solver(example_data, *args))

    puzzle_data = self.read_1(parser)
    print(solver(puzzle_data, *args))

  def part2(self, parser, solver, *args):
    print("part 2")
    
    example_data = self.read_ex2(parser)
    print(solver(example_data, *args))

    puzzle_data = self.read_2(parser)
    print(solver(puzzle_data, *args))
