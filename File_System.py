class Node:
  def __init__(self):
    self.children = {}
    self.isFile = False 
    self.content = ""

class FileSystem:
  def __init__(self):
    self.root = Node()
  
  def traverse(self, path):
    node = self.root 
    if path == "/":
      return node 
    
    for folder in path.split("/")[1:]:
      if folder not in node.children:
        node.children[folder] = Node()
      
      node = node.children[folder]
    
    return node 
  
  def ls(self, path):
    node = self.traverse(path)
    if node.isFile:
      return [path.split("/")[-1]]
    return sorted(node.children.keys())
  
  def mkdir(self, path):
    self.traverse(path)
  
  def addContentToFile(self, path, content):
    node = self.traverse(path)
    node.isFile = True 
    node.content += content 
  
  def readContentFromFile(self, path):
    node = self.traverse(path)
    return node.content 

fs = FileSystem()

fs.mkdir("/a/b")

fs.addContentToFile(
  "/a/b/file.txt",
  "Hello "
)

fs.addContentToFile(
  "/a/b/file.txt",
  "World"
)

print(fs.readContentFromFile(
  "/a/b/file.txt"
))

print(fs.ls("/"))

print(fs.ls("/a/b"))
