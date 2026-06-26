def xor1toN(n):
  if n % 4 == 0:
    return n 
  
  elif n % 4 == 1:
    return 1 
  
  elif n % 4 == 2:
    return n + 1
  
  return 0 

print(xor1toN(10))
