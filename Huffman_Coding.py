import heapq 

class Node:
  def __init__(self, freq, char=None):
    self.freq = freq 
    self.char = char 
    self.left = None 
    self.right = None 
  
  def __lt__(self, other):
    return self.freq < other.freq 

def huffman(chars, freq):
  heap = [Node(f,c) for c, f in zip(chars, freq)]
  heapq.heapify(heap)

  while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    merged = Node(left.freq + right.freq)
    merged.left = left 
    merged.right = right 

    heapq.heappush(heap, merged)
  
  return heap[0]

chars = ['a','b','c','d','e','f']
freq = [5, 9, 12, 13, 16, 45]

root = huffman(chars, freq)
print(root.freq)
