from collections import defaultdict

class TicTacToe:
  def __init__(self):
    self.grid = [["","",""],["","",""],["","",""]]
    self.row = {0: defaultdict(set), 1: defaultdict(set), 2: defaultdict(set)} # {r: {X: (()) O: (())}}
    self.col = {0: defaultdict(set), 1: defaultdict(set), 2: defaultdict(set)} # {c: {X: (()) O: (())}}
    self.diag = {0: defaultdict(set), 1: defaultdict(set)} # {d: {X: (()) O: (())}}
  
  def mark_position(self, pos, val):
    r, c = pos
    
    if self.grid[r][c] != "":
      print("This position already marked.")
      return "Marked"

    self.grid[r][c] = val

    if (r,c) not in self.row[r][val] and (r,c) not in self.col[c][val]:
      self.row[r][val].add((r,c))
      self.col[c][val].add((r,c))

    key = 0 if r == c else 1
    if (r,c) not in self.diag[key][val] and (r == c or c-r > 1 or r-c > 1):
        if (r,c) != (1,1):
          self.diag[key][val].add((r,c))
        else:
          self.diag[0][val].add((r,c))
          self.diag[1][val].add((r,c))

    self.print_grid()

    if self.check_complete():
      return "Winner is player: " + val
    elif self.isFull():
      return "Draw - play again"
    else:
      print("Mark complete")
      return ""

      
  def isFull(self):
    count = 0
    for r in range(len(self.grid)):
      for c in range(len(self.grid[0])):
        if self.grid[r][c] in ('X','O'):
          count += 1
    return True if count == 9 else False


  def check_complete(self):
    for r in range(len(self.grid)):
      for c in range(len(self.grid[0])):
        #Check rows
        if len(self.row[r]['X']) == 3 or len(self.row[r]['O']) == 3:
          return True
        #Check columns
        if len(self.col[c]['X']) == 3 or len(self.col[c]['O']) == 3:
          return True
        #Check diagnoals
        key = 0 if r == c else 1
        if len(self.diag[key]['X']) == 3 or len(self.diag[key]['O']) == 3:
          return True
          
        if "" in self.grid[r] or "" in self.grid[c]:
          continue
        elif (r == c and "" in self.grid[r][c]) or ((c-r > 1 or r-c > 1) and "" in self.grid[r][c]):
          continue
    return False


  def print_grid(self):
      return print( "\n{} \n{} \n{}".format(self.grid[0],self.grid[1],self.grid[2]))


game = TicTacToe()
result = ""
x_ya_o = 'X'
try:
  while True:
    print("Enter row val: ")
    row_input = int(input())
    print("Enter col val: ")
    col_input = int(input())

    result = game.mark_position((row_input, col_input), x_ya_o)
    if 'Marked' not in result:
      x_ya_o = 'O' if x_ya_o == 'X' else 'X'

    if 'Winner' in result or 'Draw' in result:
      break
    elif 'Marked' in result:
      continue
  print(result)

except ValueError as e:
  print("Invalid input. Error message: {}".format(e))