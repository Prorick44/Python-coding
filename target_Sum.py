def findTargetSumWays(nums, target):
  dp = {0: 1}
  for num in nums:
    nextDP = {}
    for total, count in dp.items():
      nextDP[total+num] = nextDP.get(total+num, 0) + count 
      nextDP[total-num] = nextDP.get(total - num, 0) + count 
    dp = nextDP
  
  return dp.get(target, 0)

print(findTargetSumWays([1,1,1,1,1], 3))
