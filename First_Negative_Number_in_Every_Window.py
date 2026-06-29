from collections import deque 

def firstNegative(arr, k):
  dq = deque()
  ans = []
  for i in range(len(arr)):
    if arr[i] < 0:
      dq.append(i)
    while dq and dq[0] <= i-k:
      dq.popleft()
    if i >= k-1:
      if dq:
        ans.append(arr[dq[0]])
      else:
        ans.append(0)
  
  return ans 

print(firstNegative(
  [-8,2,3,-6,10], 2
))
