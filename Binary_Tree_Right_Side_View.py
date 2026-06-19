from collections import deque 

def rightSideView(root):
  if not root:
    return []
  
  result = []
  queue = deque([root])

  while queue:
    rightNode = None 

    for _ in range(len(queue)):
      node = queue.popleft()
      rightNode = node 

      if node.left:
        queue.append(node.left)
      
      if node.right:
        queue.append(node.right)
    
    result.append(rightNode.val)
  
  return result