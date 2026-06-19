def productExceptSelf(nums):
  n = len(nums)
  ans = [1] * n 

  prefix = 1 
  for i in range(n):
    ans[i] = prefix
    prefix *= nums[i]
  
  postfix = 1 
  for i in range(n-1, -1, -1):
    ans[i] *= postfix 
    postfix *= nums[i]
  
  return ans 

nums = [1,2,3,4]
print(productExceptSelf(nums))
