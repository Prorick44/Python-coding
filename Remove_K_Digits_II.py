def removeKdigits(num, k):
  stack = []
  for digit in num:
    while k and stack and stack[-1] > digit:
      stack.pop()
      k -= 1 
    stack.append(digit)
  
  while k:
    stack.pop()
    k -= 1 
  
  ans = "".join(stack).lstrip('0')

  return ans if ans else "0"

print(removeKdigits("1432219", 3))
