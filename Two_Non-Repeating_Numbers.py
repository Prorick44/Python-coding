def twoSingles(nums):
  xor_all = 0 

  for num in nums:
    xor_all ^= num 
  
  rightmost = xor_all & -xor_all

  a = b = 0

  for num in nums:
    if num & rightmost:
      a ^= num 
    else:
      b ^= num 
  
  return a, b 

print(twoSingles([2, 4, 7, 9, 2, 4]))
