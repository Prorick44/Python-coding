n = int(input())
graph = [[] for _ in range(n)]

def dfs(node, parent, dist):
  farthest = (dist, node)

  for nxt in graph[node]:
    if nxt == parent:
      continue 

    candidate = dfs(nxt, node, dist + 1)

    if candidate[0] > farthest[0]:
      farthest = candidate
  
  return farthest

_, A = dfs(0, -1, 0)
diameter, _ = dfs(A, -1, 0)

print(diameter)
