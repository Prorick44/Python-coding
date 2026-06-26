def singleNumber(nums):
  ans = 0 

  for num in nums:
    ans ^= num 
  
  return ans 

print(singleNumber([2, 2, 1]))
