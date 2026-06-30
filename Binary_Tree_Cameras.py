camera = 0 

def dfs(root):
  global camera 

  if not root:
    return 2 
  
  left = dfs(root.left)
  right = dfs(root.right)

  if left == 0 or right == 0:
    camera += 1
    return 1 
  
  if left == 1 or right == 1:
    return 2 
  
  return 0
