# Thanks Reddit I did not know this existed
from collections import Counter     

def parseInput():
  f = open("test.txt", "r")
  lines = f.read().split("\n")
  template = lines[0]
  insertions = dict(v.split(" -> ") for v in filter(lambda x: x, lines[1:]))
  return template, insertions



def solve(rounds):
  template, insertions = parseInput()
  def count(a, b, depth=rounds):
    if depth == 0:
      return Counter('')
    key = "{}{}".format(a,b)
    if key in insertions:  
      return Counter(insertions[key]) + count(a, insertions[key], depth -1) + count(insertions[key], b, depth -1)
  c = Counter([template[0], template[-1]])
  cursor = 0
  for round in rounds:
    while cursor < len(template) - 1:
      print(cursor)
      c += count(template[cursor], template[cursor+1])
      cursor += 1
  
  
  print("Answer: {}".format(c.most_common()[0][-1] - c.most_common()[-1][-1]))


def part1():
  print('Day 14 part 1')
  solve(10)


def part2():
  print('Day 14 part 2')
  # solve(40)

def main():
  part1()
  part2()

main()

tpl, _, *rules = open("test.txt", "r").read().split('\n')
rules = dict(r.split(" -> ") for r in rules)


def f(a, b, depth=40):
    print(a,b)
    if depth == 0: return Counter('')
    x = rules[a+b]
    return Counter(x) + f(a, x, depth-1) \
                      + f(x, b, depth-1)
print(tpl, tpl[1:])
c = sum(map(f, tpl, tpl[1:]), Counter(tpl))
print(max(c.values()) - min(c.values()))

