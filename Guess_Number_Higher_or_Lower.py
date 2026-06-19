pick = 6 

def guess(num):
  if num == pick:
    return 0 
  elif num < pick:
    return 1 
  else:
    return -1 
  
def guessNumber(n):
  left, right = 1, n
  while left <= right:
    mid = (left + right) // 2 
    res = guess(mid)
    if res == 0:
      return mid 
    elif res == 1:
      left = mid + 1 
    else:
      right = mid - 1 

print(guessNumber(10))