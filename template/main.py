def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: x, filter(lambda x: x, f.read().split("\n"))))
  return l


def part1():
  print('Day 1 part 1')
  lines = parseInput()


def part2():
  print('Day 1 part 2')
  lines = parseInput()

def main():
  part1()
  part2()

main()