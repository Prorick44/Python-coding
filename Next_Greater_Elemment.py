def nextGreater(nums):
  n = len(nums)
  ans = [-1] * n 
  stack = []

  for i in range(n-1, -1, -1):
    while stack and stack[-1] <= nums[i]:
      stack.pop()
    
    if stack:
      ans[i] = stack[-1]
    
    stack.append(nums[i])
  
  return ans 

print(nextGreater([2, 1, 2, 4, 3]))