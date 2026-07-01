from functools import lru_cache


FULL = (1 << n) - 1

@lru_cache(None)
def solve(mask):
  if mask == FULL:
    return 0
  
  ans = float('inf')

  for i in range(n):
    if mask & (1 << i):
      continue 

    ans = min(
      ans,
      solve(mask | (1 << i))
    )
  
  return ans

