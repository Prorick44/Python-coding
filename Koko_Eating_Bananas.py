import math 

def minEatingSpeed(piles, h):
  left, right = 1, max(piles)
  result = right 
  while left <= right:
    k = (left + right)//2
    hours = 0 
    for pile in piles:
      hours += math.ceil(pile/k)
    if hours <= h:
      result = k 
      right = k-1
    else:
      left = k+1
  return result 

print(minEatingSpeed([3,6,7,11], 8))