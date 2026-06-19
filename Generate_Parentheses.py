def generateParenthesis(n):
  result = []
  stack = []

  def backtrack(openCount, closeCount):
    if openCount == closeCount == n:
      result.append("".join(stack))
      return
    
    if openCount < n:
      stack.append("(")
      backtrack(openCount + 1, closeCount)
      stack.pop()
    
    if closeCount < openCount:
      stack.append(")")
      backtrack(openCount, closeCount + 1)
      stack.pop()
  
  backtrack(0, 0)
  return result
    
print(generateParenthesis(3))