n = int(input())
value = [0] * n

graph = [[] for _ in range(n)]

dp = [[0, 0] for _ in range(n)]

def dfs(node, parent):
  dp[node][1] = value[node]
  for child in graph[node]:
    if child == parent:
      continue 
    dfs(child, node)
    dp[node][0] += max(
      dp[child][0],
      dp[child][1]
    )

    dp[node][1] += dp[child][0]