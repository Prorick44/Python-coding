def dailyTemperatures(temperatures):
  result = [0] * len(temperatures)
  stack = []

  for i, temp in enumerate(temperatures):
    while stack and temp > stack[-1][0]:
      stackTemp, index = stack.pop()
      result[index] = i - index 
    
    stack.append((temp, i))
  
  return result

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
