def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: x, filter(lambda x: x, f.read().split("\n"))))
  return l


def part1():
  print('Day 9 part 1')
  lines = parseInput()
  
  risk = 0
  for y, row in enumerate(lines):
    for x, char in enumerate(row):
      value = int(char)
      isLow = True
      # Above
      if y > 0 and value >= int(lines[y-1][x]):
        isLow = False
      # Below
      if y < len(lines) - 1 and value >= int(lines[y+1][x]):
        isLow = False
      # Right
      if x < len(row) - 1 and value >= int(lines[y][x+1]):
        isLow = False
      # Left
      if x > 0 and value >= int(lines[y][x-1]):
        isLow = False
      if isLow:
        risk += value + 1

  print("Answer: {}".format(risk))


def part2():
  print('Day 9 part 2')
  lines = parseInput()
  


  def bfsKinda(startX, startY):
    visited = []
    queue = []
    visited.append((startX, startY))
    queue.append((startX, startY))

    while queue:
      (x, y) = queue.pop(0) 
      neighbors = []
      # Above
      if y > 0 and lines[y - 1][x] != "9":
        neighbors.append((x, y - 1))
      # Below
      if y < len(lines) - 1 and lines[y + 1][x] != "9":
        neighbors.append((x, y + 1))
      # Right
      if x < len(lines[y]) - 1 and lines[y][x + 1] != "9":
        neighbors.append((x + 1, y))
      # Left
      if x > 0 and lines[y][x - 1] != "9":
        neighbors.append((x - 1, y))
      
      for neighbor in neighbors:
        if neighbor not in visited:
          visited.append(neighbor)
          if neighbor not in queue:
            queue.append(neighbor)
    return visited
  
  basins = []
  for y, row in enumerate(lines):
    for x, char in enumerate(row):
      if char != '9':
        basin = bfsKinda(x, y)
        possible = len(basins) < 3
        # This is not fast and could be greatly improved
        for b in basins:
          if len(basin) > len(b):
            possible = True 
        if possible:
          match = False
          for b in basins:
            innerMatch = True
            for coords in b:
              if coords not in basin:
                innerMatch = False
            if innerMatch:
              match = True
              break
          if not match:
            basins.append(basin)

  basins.sort(key=lambda x: len(x))
  
  print(len(basins[-1]) * len(basins[-2]) * len(basins[-3]))


def main():
  part1()
  part2()

main()