from collections import defaultdict 

def countComponents(n, edges):
  graph = defaultdict(list)

  for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

  visited = set()

  def dfs(node):
    if node in visited:
      return
    
    visited.add(node)

    for nei in graph[node]:
      dfs(nei)
  
  count = 0 

  for node in range(n):
    if node not in visited:
      dfs(node)
      count += 1 

  
  return count 
