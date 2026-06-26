def countbits(n):
  count = 0 

  while n:
    n &= (n - 1)
    count += 1 
  
  return count 

print(countbits(13))