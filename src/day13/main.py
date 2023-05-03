def parseInput():
  f = open("input.txt", "r")
  lines = f.read().split("\n")
  folds = list(map(lambda x: Fold(x), filter(lambda x: x and x.startswith('fold'), lines)))
  coords = set(map(lambda x: x, filter(lambda x: x and not x.startswith('fold'), lines)))
  
  return folds, coords


class Fold:
  def __init__(self, line):
    parts = line.split()
    axis, coord = parts[-1].split('=')
    self.coord = int(coord)
    self.axis = axis

def performFold(fold, coord):
  x,y = coord.split(",")
  y = int(y)
  x = int(x)
  if fold.axis == "y" and y > fold.coord:
    return "{},{}".format(x, y - (2 * (y - fold.coord)))
  if fold.axis == "x" and x > fold.coord:
    return "{},{}".format(x - (2 * (x - fold.coord)), y)
  return coord

def part1():
  print('Day 13 part 1')
  folds, coords = parseInput()
  coords = set(map(lambda x: performFold(folds[0], x), coords))
  print("Fold over {}={} | New Coords: {}".format(folds[0].axis, folds[0].coord, len(coords)))

def part2():
  print('Day 13 part 2')
  folds, coords = parseInput()
  yRange = 1000
  xRange = 1000
  for fold in folds:
    coords = set(map(lambda x: performFold(fold, x), coords))
    
    if fold.axis == "y" and yRange > fold.coord:
      yRange = fold.coord
    if fold.axis == "x" and xRange > fold.coord:
      xRange = fold.coord
      
    print("Fold over {}={} | New Coords: {}".format(fold.axis, fold.coord, len(coords)))
  
  for y in range(0,yRange):
    line = ''
    for x in range(0, xRange):
      if "{},{}".format(x,y) in coords:
        line += "#"
      else:
        line += "."
    print(line)

def main():
  part1()
  part2()

main()