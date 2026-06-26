def missingNumber(nums):
  ans = len(nums)

  for i in range(len(nums)):
    ans ^= i ^ nums[i]

  return ans 

print(missingNumber([3, 0, 1]))
