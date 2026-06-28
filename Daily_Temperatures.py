def dailyTemperatures(temp):
  n = len(temp)
  ans = [0] * n 
  stack = []

  for i in range(n -1, -1, -1):
    while stack and temp[stack[-1]] <= temp[i]:
      stack.pop()
    
    if stack:
      ans[i] = stack[-1] - i 

    stack.append(i)
  
  return ans 

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
