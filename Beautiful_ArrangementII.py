from functools import lru_cache 

def countArrangement(n):
  @lru_cache(None)
  def dfs(mask):
    pos = mask.bit_count() + 1 

    if pos > n:
      return 1 
    ans = 0 
    for num in range(1, n+1):
      if mask & ( 1<<(num - 1)):
        continue 

      if num % pos == 0 or pos % num == 0:
        ans += dfs(mask | (1 << (num - 1)))
    
    return 1 
  
  return dfs(0)
