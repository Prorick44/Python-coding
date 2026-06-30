class TarjanSCC:
  def __init__(self, n):
    self.n = n 
    self.graph = [[] for _ in range(n)]

    self.time = 0 
    self.disc = [-1] * n 
    self.low = [-1] * n 

    self.stack = []
    self.inStack = [False] * n 

    self.scc = []
  
  def addEdge(self, u, v):
    self.graph[u].append(v)
  
  def dfs(self, u):
    self.disc[u] = self.low[u] = self.time 
    self.time += 1

    self.stack.append(u)
    self.inStack[u] = True 

    for v in self.graph[u]:
      if self.disc[v] == -1:
        self.dfs(v)

        self.low[u] = min(
          self.low[u],
          self.low[v]
        )
      
      elif self.inStack[v]:
        self.low[u] = min(
          self.low[u],
          self.disc[v]
        )
    
    if self.low[u] == self.disc[u]:
      component = []
      while True:
        node = self.stack.pop()
        self.inStack[node] = False 

        component.append(node)

        if node == u:
          break 
      
      self.scc.append(component)
  
  def solve(self):
    for i in range(self.n):
      if self.disc[i] == -1:
        self.dfs(i)
    
    return self.scc 

g = TarjanSCC(5)

g.addEdge(1,0)
g.addEdge(0,2)
g.addEdge(2,1)
g.addEdge(0,3)
g.addEdge(3,4)

print(g.solve())
