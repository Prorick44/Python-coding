def isPowerOfTwo(n):
  return n > 0 and (n & (n - 1)) == 0 

print(isPowerOfTwo(16))
print(isPowerOfTwo(18))
