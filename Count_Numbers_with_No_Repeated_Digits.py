from functools import lru_cache 

def uniqueDigits(n):
  digits = list(map(int, str(n)))

  @lru_cache(None)
  def dfs(pos, mask, tight, started):
    if pos == len(digits):
      return 1 
    
    limit = digits[pos] if tight else 9 
    ans = 0 

    for d in range(limit + 1):
      if not started and d == 0:
        ans += dfs(pos+1, mask, tight and d == limit, False)
      else:
        if mask & (1 << d):
          continue 
        ans += dfs(
          pos+1,
          mask | (1 << d),
          tight and d == limit,
          True
        )
    
    return ans 
  
  return dfs(0, 0, True, False)

print(uniqueDigits(500))

        