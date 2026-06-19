def letterCombinations(digits):
  if not digits:
    return []
  
  phone = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
  }

  result = []

  def dfs(i, current):
    if len(current) == len(digits):
      result.append(current)
      return
    for ch in phone[digits[i]]:
      dfs(i+1, current+ch)
  dfs(0, "")

  return result