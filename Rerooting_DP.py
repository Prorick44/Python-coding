def dfs1(node, parent, graph):
  for child in graph[node]:
    if child == parent:
      continue
    dfs1(child, node)

def dfs2(node, parent, graph):
  for child in graph[node]:
    if child == parent:
      continue
    dfs2(child, node)
    