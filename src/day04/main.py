class Board:
  def __init__(self, lines):   
    self.board = list(map(lambda x: list(map(lambda c: int(c),  x.strip().replace("  ", " ").split(" "))), filter(lambda x: x, lines)))
    self.bingo = False
  
  def callNumber(self, num): 
    self.board = list(map(lambda row: list(map(lambda n: -1 if n == num else n, row)), self.board))

  def checkForBingo(self):
    for x in range(0, len(self.board)):
      rowBingo = True
      colBingo = True
      for y in range(0, len(self.board[x])):
        # Check Row
        if self.board[x][y] > -1:
          rowBingo = False
        # Column Bingo
        if self.board[y][x] > -1:
          colBingo = False
      if rowBingo or colBingo:
        self.bingo = True
        return True
    
    return False

  def scoreBoard(self): 
    result = 0
    for x in range(0, len(self.board)):
      for y in range(0, len(self.board[x])):
        if self.board[x][y] > 0:
          result += self.board[x][y]
    return result
  
  def printBoard(self):
    print("==========")
    for row in self.board:
      rowStr = ''
      for n in row:
        rowStr += "| {:2d} |".format(n)
      print(rowStr) 
    
def parseInput():
  f = open("input.txt", "r")
  file = list(map(lambda x: x, filter(lambda x: x, f.read().split('\n\n'))))
  balls = list(map(lambda x: int(x), file[0].split(",")))
  boards = list(map(lambda x: Board(x.split('\n')), file[1:]))
  return balls, boards


def part1():
  print('Day 1 part 1')
  balls, boards = parseInput()
  for ball in balls: 
    for board in boards: 
      board.callNumber(ball)
      if board.checkForBingo():
        print('Answer: {}'.format(board.scoreBoard() * ball))
        return 

  


def part2():
  print('Day 1 part 2')
  balls, boards = parseInput()
  for ball in balls: 
    for board in boards: 
      if not board.bingo:
        board.callNumber(ball)
        if board.checkForBingo():
          # The last printed score would be the last board to get a bingo
          print('Board Finished Score: {}'.format(board.scoreBoard() * ball))

def main():
  part1()
  part2()

main()