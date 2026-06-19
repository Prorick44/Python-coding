class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val 
    self.left = left 
    self.right = right 

class Codec:
  def serialize(self, root):
    result = []

    def dfs(node):
      if not node:
        result.append("N")
        return 
      
      result.append(str(node.val))

      dfs(node.left)
      dfs(node.right)
    
    dfs(root)

    return ",".join(result)
  
  def deseialize(self, data):
    vals = data.split(",")
    self.i = 0 

    def dfs():
      if vals[self.i] == "N":
        self.i += 1 
        return None 
    
      node = TreeNode(int(vals[self.i]))
      self.i += 1

      node.left = dfs()
      node.right = dfs()

      return node 
    
    return dfs()
  