def dfs(node, parent, graph):
  for child in graph[node]:
    if child == parent:
      continue

    dfs(child, node, graph)