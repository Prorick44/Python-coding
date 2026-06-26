class DSU:
  def __init__(self, n):
    self.parent = list(range(n))
  
  def find(self, x):
    if self.parent[x] == x:
      return x 
    
    return self.find(self.parent[x])
  
  def union(self, x, y):
    px = self.find(x)
    py = self.find(y)

    if px != py:
      self.parent[px] = py 

dsu = DSU(5)

dsu.union(0, 1)
dsu.union(1, 2)

print(dsu.find(0))
print(dsu.find(2))
