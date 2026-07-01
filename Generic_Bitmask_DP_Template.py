from functools import lru_cache 

n = 0  # set number of items
FULL = (1 << n) - 1
answer = 0  # base answer for full mask

@lru_cache(None)
def dp(mask):
  if mask == FULL:
    return answer 
  
  ans = 0 

  for nxt in range(n):
    if mask & (1 << nxt):
      continue 

    ans = max(
      ans,
      dp(mask | (1 << nxt))
    )
  
  return ans 