def trap(height):
  stack = []
  water = 0 
  for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
      top = stack.pop()
      if not stack:
        break 
      distance = i - stack[-1] - 1 
      bounded = min(height[i], height[stack[-1]]) - height[top]
      water += distance * bounded 
    stack.append(i)
  return water 

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
