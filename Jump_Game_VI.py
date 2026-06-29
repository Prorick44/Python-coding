from collections import deque 

def maxResult(nums, k):
  dq = deque([0])
  dp = nums[:]

  for i in range(1, len(nums)):
    while dq and dq[0] < i-k:
      dq.popleft()
    dp[i] += dp[dq[0]]
    while dq and dp[dq[-1]] <= dp[i]:
      dq.pop()
    dq.append(i)
  
  return dp[-1]