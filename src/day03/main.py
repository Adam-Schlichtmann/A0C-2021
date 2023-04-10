def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: int(x, 2), filter(lambda x: x, f.read().split("\n"))))
  return l


def toMaskedBin(x):
  return format(x, '012b')


def part1():
  print('Day 1 part 1')
  lines = parseInput()
  gamma = ''
  for i  in range(0, (len(toMaskedBin(lines[0])))):
    count = 0
    for value in lines: 
      
      b = value >> len(toMaskedBin(value)) - i
      r = b & 1
      if r > 0:
        count+=1
    if count > (len(lines) / 2): 
      gamma += '1'
    else:
      gamma += '0'

  epsilon = int(gamma, 2) ^ int('1' * (len(gamma)), 2)
  print("ANSWER: {}".format(epsilon * int(gamma, 2)))


def mcb(nums, index):
  countOne = 0
  for num in nums: 
    if toMaskedBin(num)[index] == '1':
      countOne += 1
  
  # Tie goes to 1
  if countOne >= len(nums) / 2:
    return '1'
  return '0'

def lcb(nums, index):
  countOne = 0
  for num in nums: 
    if toMaskedBin(num)[index] == '1':
      countOne += 1
  # Tie goes to 0
  if countOne >= len(nums) / 2:
    return '0'
  return '1'

def part2():
  print('Day 1 part 2')
  lines = parseInput()



  ox = lines
  co = lines
  
  for i in range(0, len(toMaskedBin(lines[0]))):
    if len(ox) > 1:
      commonBit = mcb(ox, i)
      ox = list(filter(lambda value: toMaskedBin(value)[i] == commonBit, ox))    
    
    if  len(co) > 1:
      leastBit = lcb(co, i)
      co = list(filter(lambda value: toMaskedBin(value)[i] == leastBit, co))    
  
  print('Answer: {}'.format(co[0] * ox[0]))
     

def main():
  part1()
  part2()

main()