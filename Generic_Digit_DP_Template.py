from functools import lru_cache 

def solve(n):
  digits = list(map(int, str(n)))

  @lru_cache(None)
  def dp(pos, tight, started):
    if pos == len(digits):
      return 1 
    
    limit = digits[pos] if tight else 9 

    ans = 0 

    for d in range(limit + 1):
      ans += dp(
        pos + 1, 
        tight and d == limit, 
        started or d != 0 
      )
    
    return ans 
  
  return dp(0, True, False)
