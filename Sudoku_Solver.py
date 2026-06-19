def solveSudoku(board):
  def valid(row, col, num):
    for i in range(9):
      if board[row][i] == num:
        return False 
      
      if board[i][col] == num:
        return False 
      
      if board[3 * (row//3)+i//3][3*(col//3)+i%3] == num:
        return False 
    
    return True 
  
  def solve():
    for row in range(9):
      for col in range(9):
        if board[row][col] == ".":
          for num in "13456789":
            if valid(row, col, num):
              board[row][col] = num 
              if solve():
                return True 
              board[row][col] = "."
          return False 
    return True
  solve()