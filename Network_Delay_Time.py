import heapq 
from collections import defaultdict

def networkDelayTime(times, n, k):
  graph = defaultdict(list)

  for u, v, w in times:
    graph[u].append((v, w))

  minHeap = [(0, k)]
  visited = set()
  time = 0 

  while minHeap:
    weight, node = heapq.heappop(minHeap)
    if node in visited:
      continue 

    visited.add(node)
    time = max(time, weight)

    for nei , w in graph[node]:
      if nei not in visited:
        heapq.heappush(minHeap, (weight + w, nei))
  
  return time if len(visited) == n else -1 


