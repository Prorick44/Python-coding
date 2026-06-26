def reverseBits(n):
  result = 0 

  for _ in range(32):
    result <<= 1 
    result |= (n & 1)
    n >>= 1 
  
  return result

print(reverseBits(43261596))
