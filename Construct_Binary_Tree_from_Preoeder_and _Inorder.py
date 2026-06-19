class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val 
    self.left = left 
    self.right = right
    
def buildTree(preorder, inorder):
  indexMap = {v: i for i, v in enumerate(inorder)}

  def helper(preL, preR, inL, inR):
    if preL > preR:
      return None 
    
    rootVal = preorder[preL]
    root = TreeNode(rootVal)

    mid = indexMap[rootVal]

    leftSize = mid - inL 

    root.left = helper(preL + 1, preL + leftSize, inL, mid - 1)

    root.right = helper(preL + leftSize + 1, preR, mid+1, inR)

    return root 
  return helper(0, len(preorder)-1, 0, len(inorder)-1)