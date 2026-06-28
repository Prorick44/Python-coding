def nextGreaterElement(nums1, nums2):
  stack = []
  mp = {}
  for num in nums2:
    while stack and stack[-1] < num:
      mp[stack.pop()] = num 
    stack.append(num)
  
  while stack:
    mp[stack.pop()] = -1 
  
  return [mp[x] for x in nums1]

print(nextGreaterElement([4,1,2],[1,3,4,2]))
