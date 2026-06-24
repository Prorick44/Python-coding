def rob(nums):
  def helper(arr):
    rob1, rob2 = 0, 0 

    for n in arr:
      temp = max(n + rob1, rob2)
      rob1 = rob2 

    return rob2 
  
  return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

print(rob([2,3,2]))