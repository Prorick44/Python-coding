class Articulation:
  def __init__(self, n):
    self.graph = [[] for _ in range(n)]

    self.disc = [-1] * n 
    self.low = [-1] * n 

    self.time = 0 
    self.answer = set()
  
  def addEdge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def dfs(self, u, parent):
    children = 0
    self.disc[u] = self.low[u] = self.time 
    self.time += 1 

    for v in self.graph[u]:
      if v == parent:
        continue 

      if self.disc[v] == -1:
        children += 1

        self.dfs(v, u)

        self.low[u] = min(
          self.low[u],
          self.low[v]
        )

        if parent != -1 and self.low[v] >= self.disc[u]:
          self.answer.add(u)
      
      else:
        self.low[u] = min(
          self.low[u],
          self.disc[v]
        )
    
    if parent == -1 and children > 1:
      self.answer.add(u)
  
  def solve(self):
    for i in range(len(self.graph)):
      if self.deisc[i] == -1:
        self.dfs(i, -1)
    
    return list(self.answer)