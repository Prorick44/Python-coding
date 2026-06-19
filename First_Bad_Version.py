bad = 4 

def isBadVersion(version):
  return version >= bad 

def firstBadVersion(n):
  left, right = 1, n 

  while left < right:
    mid = (left + right) // 2 
    if isBadVersion(mid):
      right = mid 
    else:
      left = mid + 1 
  
  return left 

print(firstBadVersion(5))
