from functools import lru_cache 

INF = float('inf')

def tsp(graph):
  n = len(graph)

  @lru_cache(None)
  def dfs(mask, city):
    if mask == (1 << n) - 1:
      return graph[city][0]
    
    ans = INF 

    for nxt in range(n):
      if mask & (1 << nxt):
        continue
      ans = min(
        ans, 
        graph[city][nxt] + 
        dfs(mask | (1 << nxt), nxt)  
      )

    return ans 
  
  return dfs(1, 0)