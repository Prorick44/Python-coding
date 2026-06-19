def maxPathSum(root):
  answer = root.val 

  def dfs(node):
    nonlocal answer 

    if not node:
      return 0
    
    left = max(dfs(node.left), 0)
    right = max(dfs(node.right), 0)

    answer = max(answer, node.val + left + right)

    return node.val + max(left, right)

  dfs(root)

  return answer