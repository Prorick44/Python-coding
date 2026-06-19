def numIslands(grid):
  rows, cols = len(grid), len(grid[0])
  visited = set()

  def dfs(r, c):
    if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == "0" or (r, c) in visited)