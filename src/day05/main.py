class Line:
  def __init__(self, line):   
    parts = line.split(" -> ")
    if len(parts) != 2:
      print('UNABLE TO PARSE LINE', line)
      exit(1)
    
    start = list(map(lambda x: int(x), parts[0].split(",")))
    end = list(map(lambda x: int(x), parts[1].split(",")))
    self.start = start
    self.end = end
  

def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: Line(x), filter(lambda x: x, f.read().split("\n"))))
  return l



N = 1000

def part1():
  print('Day 1 part 1')
  lines = parseInput()
  straightLines = list(filter(lambda x: x.start[1] == x.end[1] or x.start[0] == x.end[0] , lines))
  grid = []
  for y in range(0, N):
    row = []
    for x in range(0, N):
      row.append(0)
    grid.append(row)

  for line in straightLines: 
    if (line.start[0] == line.end[0]):
      start = line.start[1] if line.start[1] < line.end[1] else line.end[1]
      end = line.end[1] if line.end[1] > line.start[1] else line.start[1]
      for y in range(start, end + 1):
        grid[y][line.start[0]] += 1
    if (line.start[1] == line.end[1]):
      start = line.start[0] if line.start[0] < line.end[0] else line.end[0]
      end = line.end[0] if line.end[0] > line.start[0] else line.start[0]
      for x in range(start, end + 1):
        grid[line.start[1]][x] += 1

  
  count = 0
  for y in range(0, len(grid)):
    row = ""
    for x in range(0, len(grid[y])):
      row += "{}".format(grid[y][x])
      if grid[y][x] > 1:
        count+=1

  print('Answer: {}'.format(count))



def part2():
  print('Day 1 part 2')
  lines = parseInput()
  straightLines = list(filter(lambda x: x.start[1] == x.end[1] or x.start[0] == x.end[0] , lines))
  diagonalLines = list(filter(lambda x: x.start[1] != x.end[1] and x.start[0] != x.end[0] , lines))
  grid = []
  for y in range(0, N):
    row = []
    for x in range(0, N):
      row.append(0)
    grid.append(row)

  for line in straightLines: 
    if (line.start[0] == line.end[0]):
      start = line.start[1] if line.start[1] < line.end[1] else line.end[1]
      end = line.end[1] if line.end[1] > line.start[1] else line.start[1]
      for y in range(start, end + 1):
        grid[y][line.start[0]] += 1
    if (line.start[1] == line.end[1]):
      start = line.start[0] if line.start[0] < line.end[0] else line.end[0]
      end = line.end[0] if line.end[0] > line.start[0] else line.start[0]
      for x in range(start, end + 1):
        grid[line.start[1]][x] += 1

  for line in diagonalLines: 
    x = line.start[0]
    y = line.start[1]
    grid[y][x] += 1
    while (y != line.end[1] and x != line.end[0]): 
      if line.start[0] < line.end[0]:
        x+=1
      else:
        x-=1
      if line.start[1] < line.end[1]:
        y+=1
      else:
        y-=1
      grid[y][x] += 1
  
  count = 0
  for y in range(0, len(grid)):
    row = ""
    for x in range(0, len(grid[y])):
      row += "{}".format(grid[y][x])
      if grid[y][x] > 1:
        count+=1

  print('Answer: {}'.format(count))
  

def main():
  part1()
  part2()

main()