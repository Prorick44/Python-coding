from collections import defaultdict 

def criticalConnetions(n, connections):
  graph = defaultdict(list)

  for u, v in connections:
    graph[u].append(v)
    graph[v].append(u)

  disc = [-1] * n 
  low = [-1] * n 

  result = []
  time = 0 

  def dfs(node, parent):
    nonlocal time 

    disc[node] = low[node] = time 
    time += 1 

    for nei in graph[node]:
      if nei == parent:
        continue

      if disc[nei] == -1:
        dfs(nei, node)
        low[node] = min(low[node], low[nei])
        if low[nei] > disc[node]:
          result.append([node, nei])
      
      else:
        low[node] = min(low[node], disc[nei])
  
  dfs(0, -1)
  return result