import heapq 

def prim(graph, n):
  visited = [False] * n 
  pq = [(0, 0)]
  mst = 0 

  while pq:
    wt, u = heapq.heappop(pq)

    if visited[u]:
      continue 

    visited[u] = True 

    mst += wt 

    for v, w in graph[u]:
      if not visited[v]:
        heapq.heappush(pq, (w, v))
  
  return mst 
