class TrieNode:
  def __init__(self):
    self.children = {}

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, num):
    node = self.root 

    for i in range(31, -1, -1):
      bit = (num >> i) & 1 

      if bit not in node.children:
        node.children[bit] = TrieNode()
      
      node = node.children[bit]
  
  def maxXor(self, num):
    node = self.root 
    xor = 0 

    for i in range(31, -1, -1):
      bit = (num >> i) & 1 
      opposite = 1 - bit 

      if opposite in node.children:
        xor |= (1 << i)
        node = node.children[opposite]
      else:
        node = node.children[bit]

    return xor 

  def findMaximumXOR(nums):
    trie = Trie()

    for num in nums:
      trie.insert(num)

    ans = 0 

    for num in nums:
      ans = max(ans, trie.maxXor(num))

    return ans 

  print(findMaximumXOR([3,10,5,25,2,8]))
   