def monotonicStack(nums):
  stack = []
  answer = [-1] * len(nums)

  for i in range(len(nums)-1, -1, -1):
    while stack and stack[-1] <= nums[i]:
      stack.pop()
    if stack:
      answer[i] = stack[-1]
    stack.append(nums[i])
  
  return answer