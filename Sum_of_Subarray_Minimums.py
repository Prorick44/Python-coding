def sumSubarrayMins(arr):
  MOD = 10**9 + 7 
  stack = []
  result = 0 
  arr = [0] + arr + [0]
  for i, x in enumerate(arr):
    while stack and arr[stack[-1]] > x:
      mid = stack.pop()
      left = mid - stack[-1]
      right = i - mid 
      result += arr[mid] * left * right 
    
    stack.append(i)
  
  return result % MOD 

print(sumSubarrayMins([3, 1, 2, 4]))
