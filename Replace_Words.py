class TrieNode:
  def __init__(self):
    self.children = {}
    self.end = False 

def replaceWords(dictionary, sentence):
  root = TrieNode()

  for word in dictionary:
    node = root 

    for ch in word:
      if ch not in node.children:
        node.children[ch] = TrieNode()
      
      node = node.children[ch]
    
    node.end = True 
  
  def shortestRoot(word):
    node = root 
    prefix = ""

    for ch in word:
      if ch not in node.children:
        return word 
      
      node = node.children[ch]
      prefix += ch 

      if node.end:
        return prefix
    
    return word 
  
  return " ".join(shortestRoot(word) for word in sentence.split())
