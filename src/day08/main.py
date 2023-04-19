def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: Input(x), filter(lambda x: x, f.read().split("\n"))))
  return l


def sortByLen(val):
  return len(val)

class Input: 
  def __init__(self, line):
    parts = line.split(" | ")
    self.input = parts[0].split(" ")
    self.output = parts[1].split(" ")
    #  000
    # 6   1
    # 6   1
    # 6   1
    #  555
    # 4   2
    # 4   2
    # 4   2
    #  333
    # 0 appears in 0, 2, 3, 5, 6, 7, 8
    # 1 appears in 0, 1, 2, 3, 4, 7, 8
    # 2 appears in 0, 1, 3, 4, 5, 6, 7, 8
    # 3 appears in 0, 2, 3, 5, 6, 8
    # 4 appears in 0, 2, 6, 8
    # 5 appears in 2, 3, 4, 5, 6, 8
    # 6 appears in 0, 4, 5, 6, 8
    self.segments = ['', '', '', '', '', '', '']
  


  def decode(self):
    possibles = ['', '', '', '', '', '', '']
    numbers = self.input + self.output
    numbers.sort(key=sortByLen)

    ones = list(filter(lambda x: len(x) == 2, numbers))
    fours = list(filter(lambda x: len(x) == 4, numbers))
    sevens = list(filter(lambda x: len(x) == 3, numbers))
    eights = list(filter(lambda x: len(x) == 7, numbers))
        
    # len is 6 and it does NOT contain all of the chars in one
    sixes = list(filter(lambda x: len(x) == 6 and not all(map(lambda char: True if char in x else False, ones[0])) ,numbers))
    
    # Determine top segment
    for c in sevens[0]:
      if c not in ones[0]:
        possibles[0] = c
        break

    # len is 6 and it contains all of the chars in four and the top char
    nines = list(filter(lambda x: len(x) == 6 and all(map(lambda char: True if char in x else False, fours[0])) and possibles[0] in x ,numbers))
    # len is 6 and it contains all of the chars in four and the top char
    zeros = list(filter(lambda x: len(x) == 6 and x not in sixes and x not in nines, numbers))
    
    for c in eights[0]:
      # Determine middle segment
      if c not in zeros[0]:
        possibles[5] = c
      # Determine top right segment
      if c not in sixes[0]:
        possibles[1] = c
      # Determine bottom left segment
      if c not in nines[0]:
        possibles[4] = c

    # Determine bottom right
    for c in ones[0]:
      if c != possibles[1]:
        possibles[2] = c

    # Determine top left segment
    for c in fours[0]:
      if c not in ones[0] and c != possibles[5]:
        possibles[6] = c

    # Determine bottom
    for c in eights[0]:
      if c not in possibles:
        possibles[3] = c

  
    self.segments = possibles

  def getOutput(self):
    out = ""    
    for num in self.output:
      if len(num) == 2:
        out += "1"
      elif len(num) == 3:
        out += "7"
      elif len(num) == 4:
        out += "4"
      elif len(num) == 5:
        if self.segments[1] in num and self.segments[2] in num:
          out += "3"
        elif self.segments[1] in num and self.segments[2] not in num:
          out += "2"
        elif self.segments[1] not in num and self.segments[2] in num:
          out += "5"
      elif len(num) == 6:
        if self.segments[1] in num and self.segments[5] in num:
          out += "9"
        elif self.segments[1] in num:
          out += "0"
        elif self.segments[1] not in num:
          out += "6"
      elif len(num) == 7:
        out += "8"
      
    
    return int(out)


def part1():
  print('Day 1 part 1')
  inputs = parseInput()
  count = 0
  for input in inputs:
    for seq in input.output:
      if len(seq) == 2:
        count += 1
      elif len(seq) == 3:
        count += 1
      if len(seq) == 4:
        count += 1
      if len(seq) == 7:
        count += 1

  print("Answer: {}".format(count))




def part2():
  print('Day 1 part 2')
  inputs = parseInput()
  count = 0
  for input in inputs: 
    input.decode()
    count += input.getOutput()
  print("Answer: {}".format(count))


def main():
  part1()
  part2()

main()