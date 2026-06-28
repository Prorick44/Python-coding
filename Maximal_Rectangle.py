def maximalRectangle(matrix):
  if not matrix:
    return 0 
  
  n = len(matrix[0])
  heights = [0] * n 
  ans = 0 

  for row in matrix:
    for i in range(n):
      if row[i] == '1':
        heights[i] += 1 
      else:
        heights[i] = 0
    
    ans = max(ans, largestRectangleArea(heights[:]))
  
  return ans 

def largestRectangleArea(heights):
  stack = []
  maxArea = 0 
  heights.append(0)
  for i, h in enumerate(heights):
    while stack and heights[stack[-1]] > h:
      height = heights[stack.pop()]
      width = i if not stack else i - stack[-1] - 1 
      maxArea = max(maxArea, height * width)
    stack.append(i)
  return maxArea 

print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
