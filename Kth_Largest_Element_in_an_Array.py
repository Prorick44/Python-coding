import heapq 

def findKthLargest(nums, k):
  heap = []

  for num in nums:
    heapq.heappush(heap, num)

    if len(heap) > k:
      heapq.heappop(heap)
  
  return heap[0]

print(findKthLargest([3,2,1,5,6,4], 2))