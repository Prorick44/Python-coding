class Bridges:
  def __init__(self, n):
    self.graph = [[] for _ in range(n)]
    self.disc = [-1] * n 
    self.low = [-1] * n 
    self.time = 0
    self.answer = []
  
  def addEdge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def dfs(self, u, parent):
    self.disc[u] = self.low[u] = self.time 
    self.time += 1 

    for v in self.graph[u]:
      if v == parent:
        continue 

      if self.disc[v] == -1:
        self.dfs(v, u)

        self.low[u] = min(
          self.low[u],
          self.low[v]
        )

        if self.low[v] > self.disc[u]:
          self.low[u] = min(
            self.low[u],
            self.disc[v]
          )
  
  def solve(self):
    for i in range(len(self.graph)):
      if self.disc[i] == -1:
        self.dfs(i, -1)
    
    return self.answer 
  
g = Bridges(5)

g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print(g.solve())
