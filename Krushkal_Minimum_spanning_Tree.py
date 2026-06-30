class DSU:
  def __init__(self, n):
    self.parent = list(range(n))
  
  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    
    return self.parent[x]

  def union(self, x, y):
    px = self.find(x)
    py = self.find(y)

    if px == py:
      return False 
    
    self.parent[px] = py 
    return True
  
def krushkal(n, edges):
  edges.sort(key=lambda x: x[2])
  dsu = DSU(n)
  cost = 0 

  for u, v, w in edges:
    if dsu.union(u, v):
      cost += w 
  
  return cost 
