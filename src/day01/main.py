def parseInput():
  f = open("./src/day01/input.txt", "r")
  l = list(map(lambda x: int(x), filter(lambda x: x, f.read().split("\n"))))
  return l


def part1():
  print('Day 1 part 1')
  lines = parseInput()
  count = 0
  for x in range(1, len(lines)):
    if lines[x-1] < lines[x]:
      count += 1
  print("ANSWER: {}".format(count))
      



def part2():
  print('Day 1 part 2')
  lines = parseInput()

  count = 0
  for x in range(len(lines) - 3):
    first = lines[x] + lines[x+1] + lines[x+2]
    second = lines[x+1] + lines[x+2] + lines[x+3]
    if first < second:
      count += 1
  print("ANSWER: {}".format(count))

def main():
  part1()
  part2()

main()