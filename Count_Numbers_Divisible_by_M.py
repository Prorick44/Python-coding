from functools import lru_cache 

def divisibleByM(n, m):
  digits = list(map(int, str(n)))

  @lru_cache(None)
  def dfs(pos, rem, tight):
    if pos == len(digits):
      return 1 if rem == 0 else 0 
    
    limit = digits[pos] if tight else 9 

    ans = 0 

    for d in range(limit + 1):
      ans += dfs(
        pos + 1, 
        (rem * 10 + d) % m,
        tight and d == limit
      )
    
    return ans 
  
  return dfs(0, 0, True)
