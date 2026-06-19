class TrieNode:
  def __init__(self):
    self.children = {}
    self.word = None 

def findWords(board, words):
  root = TrieNode()
  for word in words:
    node = root 
    for ch in word:
      if ch in node.children:
        node.children[ch] = TrieNode()
      
      node = node.children[ch]
    node.word = word 
  
  rows, cols = len(board), len(board[0])

  result = []

  def dfs(r, c, node):
    letter = board[r][c]
    if letter not in node.children:
      return
    nxt = node.children[letter]
    if nxt.word:
      result.append(nxt.word)
      nxt.word = None 
    
    board[r][c] = "#"
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for dr, dc in directions:
      nr = r + dr 
      nc = c + dc 

      if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
        dfs(nr, nc, nxt)
    board[r][c] = letter 

  for r in range(rows):
    for c in range(cols):
      dfs(r, c, root)
  
  return result 
