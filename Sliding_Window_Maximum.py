from collections import deque 

def maxSlidingWindow(nums, k):
  q = deque()
  result = []
  for i in range(len(nums)):
    q = deque()
    result = []

    for i in range(len(nums)):
      while q and q[0] <= i-k:
        q.popleft()
      while q and nums[q[-1]] < nums[i]:
        q.pop()
      q.append(i)
      if i >= k-1:
        result.append(nums[q[0]])
  return result

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7]))
