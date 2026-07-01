class LRUCache:
  class Node:
    def __init__(self, key, val):
      self.key = key 
      self.val = val 
      self.prev = None 
      self.next = None 
  
  def __init__(self, capacity):
    self.capacity = capacity 

    self.map = {}

    self.head = self.Node(0, 0)
    self.tail = self.Node(0, 0)

    self.head.next = self.tail 
    self.tail.prev = self.head 
  
  def remove(self, node):
    p = node.prev 
    n = node.next 

    p.next = n 
    n.prev = p 

  def insert(self, node):
    node.next = self.head.next 
    node.prev = self.head 

    self.head .next.prev = node 
    self.head.next = node

  def get(self, key):
    if key not in self.map:

      return -1
    node = self.map[key]
    self.remove(node)
    self.insert(node)

    return node.val
  
  def put(self, key, value):
    if key in self.map:
      node = self.map[key]
      self.remove(node)
      del self.map[node.key]
    
    node = self.Node(key, value)

    self.map[key] = node 

    self.insert(node)


cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1)) 

cache.put(3,3)
print(cache.get(2))

cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
