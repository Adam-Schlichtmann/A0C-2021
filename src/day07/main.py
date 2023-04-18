import sys 

def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: x, filter(lambda x: x, f.read().split("\n"))))
  n = list(map( lambda x: int(x), l[0].split(",")))
  return n

def part1():
  print('Day 7 part 1')
  crabs = parseInput()
  max = -sys.maxsize-1
  min = sys.maxsize
  for crab in crabs:
    if crab > max:
      max = crab
    if crab < min:
      min = crab
  
  cheapest = sys.maxsize
  for position in range(min, max):
    cost = 0
    for crab in crabs:
      cost += abs(position - crab)
    if cost < cheapest:
      cheapest = cost

  print("Answer: {}".format(cheapest))

def part2():
  print('Day 7 part 2')
  crabs = parseInput()
  max = -sys.maxsize-1
  min = sys.maxsize
  for crab in crabs:
    if crab > max:
      max = crab
    if crab < min:
      min = crab
  
  print(min, max)
  cheapest = sys.maxsize
  for position in range(min, max):
    cost = 0
    for crab in crabs:
      diff = abs(position - crab) + 1
      cost += (diff * (diff - 1)) / 2
    if cost < cheapest:
      cheapest = cost

  # to low 98564235
  print("Answer: {}".format(cheapest))

def main():
  part1()
  part2()

main()