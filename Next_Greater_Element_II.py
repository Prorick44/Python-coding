def nextGreaterElements(nums):
  n = len(nums)
  ans = [-1] * n 
  stack = [] 
  for i in range(2 * n - 1, -1, -1):
    while stack and stack[-1] <= nums[i % n]:
      stack.pop()
    
    if i < n and stack:
      ans[i] = stack[-1]
    
    stack.append(nums[i % n])
  
  return ans 

print(nextGreaterElements([1, 2, 1]))