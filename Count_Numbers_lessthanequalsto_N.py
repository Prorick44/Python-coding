from functools import lru_cache 

def countNumbers(n):
  digits = list(map(int, str(n)))

  @lru_cache(None)
  def dfs(pos, tight):
    if pos == len(digits):
      return 1 
    
    limit = digits[pos] if tight else 9 

    ans = 0 

    for d in range(limit + 1):
      if pos == len(digits):
        return 1 
      
      limit = digits[pos] if tight else 9 
      ans = 0 
      for d in range(limit + 1):
        ans += dfs(
          pos + 1,
          tight and d == limit 
        ) 
      
      return ans 
    
    return dfs(0, True)
  
  print(countNumbers(543))