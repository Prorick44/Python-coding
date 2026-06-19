def combinationSum(candidates, target):
  result = []
  def dfs(i, current, total):
    if total == target:
      result.append(current.copy())
      return
    if i >= len(candidates) or total > target:
      return 
    
    current.append(candidates[i])
    dfs(i, current, total + candidates[i])

    current.pop()
    dfs(i+1, current, total)
  
  dfs(0, [], 0)

  return result

print(combinationSum([2,3,6,7], 7))