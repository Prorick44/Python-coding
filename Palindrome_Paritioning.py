def partition(s):
  result = []
  part = []

  def isPalindrome(left, right):
    while left < right:
      if s[left] != s[right]:
        return False 
      
      left += 1 
      right -= 1 
    
    return True 
  
  def dfs(index):
    if index >= len(s):
      result.append(part.copy())
      return 
    
    for j in range(index, len(s)):
      if isPalindrome(index, j):
        part.append(s[index:j+1])
        dfs(j+1)
        part.pop()
  
  dfs(0)
  return result