from collections import deque 

def constrainedSubsetSum(nums, k):
  dq = deque()
  dp = nums[:]
  ans = max(nums)
  for i in range(len(nums)):
    if dq:
      dp[i] = max(dp[i], nums[i]+dp[dq[0]])
    
    ans = max(ans, dp[i])
     
    while dq and dp[dq[-1]] <= dp[i]:
      dp.pop()
    
    if dp[i] > 0:
      dq.append(i)
    
    if dq and dq[0] <= i-k:
      dq.popleft()
  
  return ans 
