def parseInput():
  f = open("input.txt", "r")
  l = list(map(lambda x: x, filter(lambda x: x, f.read().split("\n"))))
  return l

def syntaxScore(char):
  if char == ")":
    return 3
  if char == "]": 
    return 57 
  if char == "}":
    return 1197
  if char == ">":
    return 25137
  
def remove(line, i):
  return line[0:i - 1] + line[i + 1:]

start = ["{", "[", "<", "("]
def cleanRow(line, i = 1):
  if i >= len(line):
    print("OUT OF INDEX")
    return 0
  if line[i] in start:
    return cleanRow(line, i+1)
  
  if line[i - 1] == "(" and line[i] == ")":
    return cleanRow(remove(line, i), i - 1)
  
  if line[i - 1] == "[" and line[i] == "]":
    return cleanRow(remove(line, i), i - 1)
  
  if line[i - 1] == "<" and line[i] == ">":
    return cleanRow(remove(line, i), i - 1)
  
  if line[i - 1] == "{" and line[i] == "}":
    return cleanRow(remove(line, i), i - 1)

  return syntaxScore(line[i])

def removePairs(line):
  line = line.replace("()", "")
  line = line.replace('{}', "")
  line = line.replace("<>", "")
  line = line.replace("[]", "")
  return line

def completeRow(line): 
  delta = 1
  while delta > 0:
    old = len(line)
    line = removePairs(line)
    delta = old - len(line)
  return line

def autocompleteScore(char):
  if char == ")":
    return 1
  if char == "]": 
    return 2 
  if char == "}":
    return 3
  if char == ">":
    return 4

def getCompletionScore(cleaned):
  score = 0
  for c in cleaned:
    score *= 5
    if c == "(":
      score += autocompleteScore(")")
    elif c == "{":
      score += autocompleteScore("}")
    elif c == "[":
      score += autocompleteScore("]")
    elif c == "<":
      score += autocompleteScore(">")
  return score


def part1():
  print('Day 10 part 1')
  lines = parseInput()
  total = 0
  for line in lines:
    score = cleanRow(line)
    total += score
  print("ANSWER: {}".format(total))

def part2():
  print('Day 10 part 2')
  scores = []
  lines = parseInput()
  for line in lines:
    score = cleanRow(line)
    if score == 0:
      cleaned = completeRow(line)
      scores.append(getCompletionScore(cleaned[::-1]))
  scores.sort()
  
  print("ANSWER: {}".format(scores[len(scores) // 2]))

def main():
  part1()
  part2()

main()