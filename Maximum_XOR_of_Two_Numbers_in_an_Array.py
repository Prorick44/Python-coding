class TrieNode:
  def __init__(self):
    self.children = {}
  
def findMaximunXOR(nums):
  root = TrieNode()
  for num in nums:
    node = root
    for i in range(31, -1, -1):
      bit = (num >> i) & 1 
      if bit not in node.children:
        node.children[bit] = TrieNode()
      node = node.children[bit]
  
  answer = 0 

  for num in nums:
    node = root 
    currXor = 0 

    for i in range(31, -1, -1):
      bit (num >> i) & 1 
      opposite = 1 - bit 

      if opposite in node.children:
        currXor |= (1 << i)
        node = node.children[bit]

    answer = max(answer, currXor)
  
  return answer 