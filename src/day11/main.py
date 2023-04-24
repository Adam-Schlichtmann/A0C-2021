def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: list(map(lambda y: int(y), x)), filter(lambda x: x, f.read().split("\n"))))

  return l

class Cave:
  def __init__(self, grid):
    self.grid = grid
    self.flashes = 0

  def findNine(self):
    for y, row in enumerate(self.grid):
      for x, item in enumerate(row):
        if item > 9:
          return y, x
    return -1, -1
  
  def flash(self, y, x):
    self.flashes += 1
    self.grid[y][x] = 0
    for dy in range(-1, 2):
      for dx in range(-1, 2):
        if dy != 0 or dx != 0:
          ny = y + dy
          nx = x + dx
          if ny >= 0 and nx >= 0 and ny < len(self.grid) and nx < len(self.grid[ny]):
            if self.grid[ny][nx] != 0: 
              self.grid[ny][nx] += 1
  
  def increase(self):
    for y in range(0, len(self.grid)):
      for x in range(0, len(self.grid[y])):
        self.grid[y][x] += 1

  def round(self):
    self.increase()
    y, x = self.findNine()
    count = 0
    while y >= 0 and x >= 0:
      count += 1
      self.flash(y, x)
      y, x = self.findNine()

def part1():
  print('Day 11 part 1')
  lines = parseInput()
  cave = Cave(lines)

  for round in range(0, 100):
    cave.round()
  
  print("ANSWER: {}".format(cave.flashes))

def part2():
  print('Day 11 part 2')
  lines = parseInput()
  cave = Cave(lines)

  for round in range(1, 1000):
    if round % 100 == 0:
      print("ROUND {}".format(round))
    old = cave.flashes
    cave.round()
    if cave.flashes - old == 100:
      print("ANSWER: {}".format(round))
      return

def main():
  part1()
  part2()

main()