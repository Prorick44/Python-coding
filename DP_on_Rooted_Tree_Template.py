n = int(input())
graph = [[] for _ in range(n)]
value = list(map(int, input().split()))
dp = [0] * n 

def dfs(node, parent):
  dp[node] = value[node]
  for child in graph[node]:
    if child == parent:
      continue

    dfs(child, node)
    dp[node] += dp[child]