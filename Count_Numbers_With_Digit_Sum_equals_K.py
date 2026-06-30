from functools import lru_cache 

def countDigitSum(n, target):
  digits = list(map(int, str(n)))

  @lru_cache(None)
  def dfs(pos, sum_so_far, tight):
    if pos == len(digits):
      return 1 if sum_so_far == target else 0 
    
    limit = digits[pos] if tight else 9 
    ans = 0 
    for d in range(limit + 1):
      ans += dfs(
        pos + 1,
        sum_so_far + d,
        tight and d == limit 
      )
    
    return ans 
  
  return dfs(0, 0, True)

print(countDigitSum(1000, 5))
