def subsetsWithDup(nums):
  nums.sort()
  result = []

  def dfs(index, subset):
    result.append(subset.copy())
    for i in range(index, len(nums)):
      if i > index and nums[i] == nums[i - 1]:
        continue
      subset.append(nums[i])
      dfs(i+1, subset)
      subset.pop()
  dfs(0, [])
  return result