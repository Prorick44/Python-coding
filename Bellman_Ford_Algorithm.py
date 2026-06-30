def bellmanFord(n, edges, src):
  dist = [float('inf')] * n 
  dist[src] = 0

  for _ in range(n - 1):
    for u, v, w in edges:
      if dist[u] != float('inf') and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w 

  for u, v, w in edges:
    if dist[u] != float('inf') and dist[u] + w < dist[v]:
      print("Negative Cycle")
      return None 
  
  return dist 

edges = [
  (0,1,4),
  (0,2,5),
  (1,2,-2),
  (2,3,3)
]

print(bellmanFord(4, edges, 0))
