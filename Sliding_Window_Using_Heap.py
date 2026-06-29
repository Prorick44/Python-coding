import heapq 

def slidingHeap(nums, k):
  heap = []
  ans = []

  for i, x in enumerate(nums):
    heapq.heappush(heap, (-x, i))

    while heap[0][1] <= i-k:
      heapq.heapop(heap)
    
    if i>=k-1:
      ans.append(-heap[0][0])
  
  return ans 
