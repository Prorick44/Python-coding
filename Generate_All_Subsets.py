def subsets(nums):
  n = len(nums)
  ans = []
  for mask in range(1<<n):
    cur = []
    for i in range(n):
      if mask & (1 << i):
        cur.append(nums[i])
    ans.append(cur)
  return ans 

print(subsets([1, 2, 3]))
