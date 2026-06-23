from collections import defaultdict, deque 

def findMinHeightTrees(n, edges):
  if n == 1:
    return [0]
  
  graph = defaultdict(list)
  degree = [0] * n 

  for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

    degree[u] += 1 
    degree[v] += 1 

  queue = deque()
  for i in range(n):
    if degree[i] == 1:
      queue.append(i)
  
  while n > 2:
    size = len(queue)
    n -= size 

    for _ in range(size):
      node = queue.popleft()

      for nei in graph[node]:
        degree[nei] -= 1

        if degree[nei] == 1:
          queue.append(nei)
  
  return list(queue)
