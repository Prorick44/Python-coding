import heapq 

def dijkstra(n, graph, src):
  dist = [float('inf')] * n 
  dist[src] = 0 

  pq = [(0, src)]

  while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
      continue

    for v, w in graph[u]:
      if dist[v] > d + w:
        dist[v] = d + w 
        heapq.heappush(pq, (dist[v], v))
  
  return dist 

graph = {
  0: [(1, 4), (2, 1)],
  1: [(3, 1)],
  2: [(1, 2), (3, 5)],
  3: []
}

print(dijkstra(4, graph, 0))