def solveNQueens(n):
  col = set()
  posDiag = set()
  negDiag = set()

  board = [["."] * n for _ in range(n)]
  result = []

  def backtrack(row):
    if row == n:
      copy = ["".join(r) for r in board]
      result.append(copy)
      return
    
    for c in range(n):
      if (
        c in col or 
        (row+c) in posDiag or
        (row-c) in negDiag
      ):
        continue 

      col.add(c)
      posDiag.add(row+c)
      negDiag.add(row-c)

      board[row][c] = "Q"

      backtrack(row+1)

      col.remove(c)
      posDiag.remove(row+c)
      negDiag.remove(row-c)

      board[row][c] = "."
  
  backtrack(0)

  return result