def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: x, filter(lambda x: x, f.read().split("\n"))))
  n = list(map( lambda x: int(x), l[0].split(",")))
  return n


class LanternFish():
  def __init__(self, nums):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]  
    for n in nums:
      counts[n] += 1
    self.counts = counts
  
  def year(self):
    newCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
    for i in range(0, len(self.counts)):
      if i == 0:
        newCounts[8] += self.counts[i]
        newCounts[6] += self.counts[i]
      else:
        newCounts[i-1] += self.counts[i]
    self.counts = newCounts

  def sum(self):
    temp = 0
    for n in self.counts:
      temp += n
    return temp
  

def part1():
  print('Day 1 part 1')
  nums = parseInput()

  fish = LanternFish(nums)
  for day in range(0, 80):
    fish.year()
    
  print("Answer: {}".format(fish.sum()))


def part2():
  print('Day 1 part 1')
  nums = parseInput()

  fish = LanternFish(nums)
  for day in range(0, 256):
    fish.year()
    
  print("Answer: {}".format(fish.sum()))
  

def main():
  part1()
  part2()

main()