class TrieNode:
  def __init__(self):
    self.children = {}
    self.end = False 

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()
  
  def addWord(self, word):
    curr = self.root
    for ch in word:
      if ch not in curr.children:
        curr.children[ch] = TrieNode()
      
      curr = curr.children[ch]
    
    curr.end = True 
  
  def search(self, word):
    def dfs(j, node):
      curr = node 
      for i in range(j, len(word)):
        c = word[i]
        if c == ".":
          for child in curr.children.values():
            if dfs(i+1, child):
              return True 
          
          return False 
        else:
          if c not in curr.children:
            return False 
          curr = curr.children[c]
      return curr.end 
    return dfs(0, self.root)
  
