def previousSmaller(nums):
  stack = []

  ans = [-1] * len(nums)
  
  for i in range(len(nums)):
    while stack and stack[-1] >= nums[i]:
      stack.pop()
    
    if stack:
      ans[i] = stack[-1]
    
    stack.append(nums[i])
  
  return ans 