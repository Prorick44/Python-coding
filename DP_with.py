from functools import lru_cache 

cost = []
n = 0
FULL = 0

@lru_cache(None)
def dfs(mask, pos):
  if mask == FULL:
    return 0 
  
  ans = float('inf')

  for nxt in range(n):
    if mask & (1 << nxt):
      continue

    ans = min(
      ans,
      cost[pos][nxt] + 
      dfs(mask | (1 << nxt), nxt)
    )
  
  return ans 