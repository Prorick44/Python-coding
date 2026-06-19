def combinationSum2(candidates, target):
  candidates.sort()
  result = []

  def backtrack(start, path, terget):
    if terget == 0:
      result.append(path[:])
      return
    
    for i in range(start, len(candidates)):
      if i > start and candidates[i] == candidates[i-1]:
        continue 
      if candidates[i] > target:
        break 
      path.append(candidates[i])
      backtrack(i+1, path, target - candidates[i])
      path.pop()
  
  backtrack(0, [], target)

  return result