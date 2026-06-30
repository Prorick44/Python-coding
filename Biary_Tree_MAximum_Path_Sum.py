answer = float('-inf')

def dfs(root):
  global answer 

  if not root:
    return 0
  
  left = max(0, dfs(root.left))
  right = max(0, dfs(root.right))

  answer = max(
    answer,
    root.val + left + right 
  )

  return root.val + max(left, right)
