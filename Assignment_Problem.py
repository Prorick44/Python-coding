from functools import lru_cache 

def assignmeent(cost):
  n = len(cost)
  @lru_cache(None)
  def dfs(mask):
    worker = mask.bit_count()
    if worker == n:
      return 0 
    ans = float('inf')
    for job in range(n):
      if mask & (1 << job):
        continue 
      ans = min(
        ans, 
        cost[worker][job] + 
        dfs(mask | ( 1<< job))
      )
    return ans 
  
  return dfs(0)

