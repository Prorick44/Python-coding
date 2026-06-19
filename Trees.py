class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val 
    self.left = left 
    self.right = right 

def invertTree(root):
  if not root:
    return None 
  
  root.left, root.right = root.right, root.left 

  invertTree(root.left)
  invertTree(root.right)

  return root 

def maxDepth(root):
  if not root:
    return 0 
  return 1 + max(maxDepth(root.left), maxDepth(root.right))

def diameterOfBinaryTree(root):
  diameter = 0 

  def dfs(node):
    nonlocal diameter 

    if not node:
      return 0 
    
    left = dfs(node.left)
    right = dfs(node.right)

    diameter = max(diameter, left + right)

    return 1 + max(left, right)
  
  dfs(root)

  return diameter

def isBalanced(root):
  def dfs(node):
    if not node:
      return [True, 0]
    
    leftBalanced, leftHeight = dfs(node.left)
    rightBalanced, rightHeight = dfs(node.right)

    balanced = (
      leftBalanced and 
      rightBalanced and 
      abs(leftHeight - rightHeight) <= 1 
    )

    return [balanced, 1 + max(leftHeight, rightHeight)]

  return dfs(root)[0]

def isSameTree(p, q):
  if not p and not q:
    return True 
  
  if not p or not q:
    return False 
  
  if p.val != q.val:
    return False 
  
  return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSubtree(root, subRoot):
  def sameTree(a, b):
    if not a and not b:
      return True 

    if not a or not b:
      return False 
    
    if a.val != b.val:
      return False
    
    return sameTree(a.left, b.left) and sameTree(a.right, b.right)
  
  if not subRoot:
    return True 
  
  if not root:
    return False 
  
  if sameTree(root, subRoot):
    return True 
  
  return (
    isSubtree(root.left, subRoot)
    or 
    isSubtree(root.right, subRoot)
  )

def lowestCommonAncestor(root, p, q):
  while root:
    if p.val < root.val and q.val < root.val:
      root = root.left 
    
    elif p.val > root.val and q.val > root.val:
      root = root.right 
    
    else:
      return root 
    