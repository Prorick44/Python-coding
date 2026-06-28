def stockSpan(price):
  stack = []
  ans = [] 

  for i, p in enumerate(price):
    while stack and price[stack[-1]] <= p:
      stack.pop()
    
    if not stack:
      ans.append(i + 1)
    else:
      ans.append(i - stack[-1])
    stack.append(i)
  
  return ans 

print(stockSpan([100, 80, 60, 75, 85]))