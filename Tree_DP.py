n = int(input())
graph = [[] for _ in range(n)]
subtree = [0] * n
value = [0] * n

def dfs(node, parent):
  subtree[node] = value[node]
  for child in graph[node]:
    if child == parent:
      continue 
    dfs(child, node)
    subtree[node] += subtree[child]