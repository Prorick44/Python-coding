def canPartition(nums):
  total = sum(nums)

  if total % 2:
    return False 
  
  target = total // 2 
  dp = {0}
  for num in nums:
    nextDp = dp.copy()
    for t in dp:
      if t + num == target:
        return True 
      
      nextDp.add(t + num)
    
    dp = nextDp 
  
  return target in dp 

print(canPartition([1,5,11,5]))
