def maxProduct(nums):
  res = max(nums)
  curMin, curMax = 1, 1 
  for n in nums:
    temp = curMax * n 

    curMax = max(n, temp, curMin*n)
    curMin = min(n, temp, curMin*n)

    res = max(res, curMax)
  
  return res 

print(maxProduct([2,3,-2,4]))
