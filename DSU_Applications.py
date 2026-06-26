from collections import defaultdict 

class DSU:
  def __init__(self, n):
    self.parent = list(range(n))
    self.size = [1] * n 

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])

    return self.parent[x]

  def union(self, x, y):
    px = self.find(x)
    py = self.find(y)

    if px == py:
      return False 

    if self.size[px] < self.size[py]:
      self.parent[px] = py 
    elif self.size[px] > self.size[py]:
      self.parent[py] = px
    else:
      self.parent[py] = px 
      self.size[px] += 1
    return True 

def countComponents(n, edges):
  dsu = DSU(n)

  components = n 

  for u, v in edges:
    pu = dsu.find(u)
    pv = dsu.find(v)

    if pu != pv:
      dsu.union(u, v)
      components -= 1

  return components 

def hascycle(n, edges):
  dsu = DSU(n)

  for u, v in edges:
    if dsu.find(u) == dsu.find(v):
      return True 
    
    dsu.union(u, v)
  
  return False

def findRedundantConnection(self, edges):
  n = len(edges)

  dsu = DSU(n + 1)

  for u, v in edges:
    if dsu.find(u) == dsu.find(v):
      return [u, v]
    dsu.union(u, v)

def findCircleNum(isConnected):
  n = len(isConnected)
  dsu = DSU(n)
  provinces = n 

  for i in range(n):
    for j in range(i+1, n):
      if isConnected[i][j]:
        if dsu.find(i) != dsu.find(j):
          dsu.union(i, j)
          provinces -= 1 
  
  return provinces 

def krushkal(n, edges):
  edges.sort(key=lambda x: x[2])
  dsu = DSU(n)
  mst_cost = 0 
  for u, v, w in edges:
    if dsu.find(u) != dsu.find(v):
      dsu.union(u, v)
      mst_cost += w 
  return mst_cost

def accountMerge(accounts):
  dsu = DSU(len(accounts))
  email_owner = {}
  for i, account in enumerate(accounts):
    for email in account[1:]:
      if email in email_owner:
        dsu.union(i, email_owner[email])
      email_owner[email] = i

  groups = defaultdict(list)

  for email, idx in email_owner.items():
    root = dsu.find(idx)
    groups[root].append(email)
  result = []

  for root, emails in groups.items():
    result.apppend(
      [accounts[root][0]] + sorted(emails)
    )
  
  return result

edges = [
  [0,1],
  [1,2],
  [2,0]
]

edges2 = [
  [0, 1, 10],
  [0, 2, 6],
  [0, 3, 5],
  [1, 3, 15],
  [2, 3, 4]
]

print(hascycle(3, edges))
print(krushkal(4, edges2))