import heapq 

def findMaximizedCapital(k, w, profits, capital):
  projects = list(zip(capital, profits))
  projects.sort()

  maxHeap = []
  i = 0

  for _ in range(k):
    while i < len(projects) and projects[i][0] <= w:
      heapq.heappush(maxHeap, -projects[i][1])
      i += 1 
    
    if not maxHeap:
      break 

    w += -heapq.heappop(maxHeap)
  
  return w 

print(findMaximizedCapital(
  2, 0, [1,2,3], [0,1,1]
))