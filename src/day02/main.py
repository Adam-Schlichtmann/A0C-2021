
class Instruction:
  def __init__(self, string):
    parts = string.split(" ")
    self.direction = parts[0]
    self.distance = int(parts[1])


def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: Instruction(x), filter(lambda x: x, f.read().split("\n"))))
  return l


def part1():
  print('Day 2 part 1')
  instructions = parseInput()
  depth = 0
  horizontal = 0
  for instruction in instructions:
    if instruction.direction == "forward":
      horizontal += instruction.distance
    elif instruction.direction == "down":
      depth += instruction.distance
    elif instruction.direction == "up":
      depth -= instruction.distance
  
  print("Answer: {}".format(depth * horizontal))


def part2():
  print('Day 2 part 2')
  instructions = parseInput()
  depth = 0
  horizontal = 0
  aim = 0
  for instruction in instructions:
    if instruction.direction == "forward":
      horizontal += instruction.distance
      depth += instruction.distance * aim
    elif instruction.direction == "down":
      aim += instruction.distance
    elif instruction.direction == "up":
      aim -= instruction.distance
  
  print("Answer: {}".format(depth * horizontal))

def main():
  part1()
  part2()

main()