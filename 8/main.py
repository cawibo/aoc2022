"""
Advent of Code 2022, day 8 : Treetop Tree House

The elfs are looking for the best tree to put a tree house in.
"""

from aoc import solver
s = solver.Solver('8')


def parse(file):
    return [[int(c) for c in line.strip()] for line in file.readlines()]


def solve1(grid):
    """calculates how many trees are visible from outside the grid"""
    height = len(grid)
    width = len(grid[0])

    visible = height * 2 + (width - 2) * 2
    visibleCoords = set()

    def toKey(row, col): return f"{row},{col}"

    # trees vissible from the left
    for i in range(1, height - 1):
        left = grid[i][0]
        for j in range(1, width - 1):
            curr = grid[i][j]
            if (curr > left):
                key = toKey(i, j)
                visibleCoords.add(key)

                left = curr

    # trees visible from the top
    for j in range(1, width - 1):
        top = grid[0][j]
        for i in range(1, height - 1):
            curr = grid[i][j]
            if (curr > top):
                key = toKey(i, j)
                visibleCoords.add(key)

                top = curr

    # mirrored grid and toKey
    grid = [line[::-1] for line in grid[::-1]]
    def toKey(row, col): return f"{height - row - 1},{width - col - 1}"

    # trees visible from the rigth
    for i in range(1, height - 1):
        right = grid[i][0]
        for j in range(1, width - 1):
            curr = grid[i][j]
            if (curr > right):
                key = toKey(i, j)
                visibleCoords.add(key)

                right = curr

    # trees visible from the bottom
    for j in range(1, width - 1):
        bottom = grid[0][j]
        for i in range(1, height - 1):
            curr = grid[i][j]
            if curr > bottom:
                key = toKey(i, j)
                visibleCoords.add(key)

                bottom = curr

    return visible + len(visibleCoords)


def getViewingDistance(grid, row, col):
    """calculates how many trees are visible from a given tree"""
    width = len(grid[0])
    height = len(grid)

    tree_height = grid[row][col]

    right = 0
    left = 0
    top = 0
    bottom = 0

    for ci in range(col+1, width):
        if grid[row][ci] >= tree_height:
            right += 1
            break
        right += 1

    for ci in range(col-1, -1, -1):
        if grid[row][ci] >= tree_height:
            left += 1
            break
        left += 1

    for ri in range(row+1, height):
        if grid[ri][col] >= tree_height:
            bottom += 1
            break
        bottom += 1

    for ri in range(row-1, -1, -1):
        if grid[ri][col] >= tree_height:
            top += 1
            break
        top += 1

    return right * left * top * bottom


def solve2(grid):
    """calculates the greatest viewing distance of any tree in the grid

    viewing distance is the product of the number of trees that can be seen in each direction"""
    width = len(grid[0])
    height = len(grid)

    greatest_viewing_distance = 0

    for row in range(height):
        for col in range(width):
            viewing_distance = getViewingDistance(grid, row, col)

            if viewing_distance > greatest_viewing_distance:
                greatest_viewing_distance = viewing_distance

    return greatest_viewing_distance


s.part1(parse, solve1)
print()
s.part2(parse, solve2)
