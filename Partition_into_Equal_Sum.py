from functools import lru_cache 

def canPartition(nums):
  total = sum(nums)

  if total % 2:
    return False 
  
  target = total // 2

  @lru_cache(None)
  def dfs(mask, s):
    if s == target:
      return True 
    
    if s > target:
      return False
    
    for i in range(len(nums)):
      if mask & (1 << i):
        continue

      if dfs(mask | (1 << i), s + nums[i]):
        return True 
    
    return False 
  return dfs(0, 0)
