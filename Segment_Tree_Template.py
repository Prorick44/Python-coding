class SegmentTree:
  def __init__(self, nums):
    self.n = len(nums)
    self.tree = [0] * (4 * self.n)
    self.build(nums, 1, 0, self.n - 1)
  
  def build(self, nums, node, l, r):
    if l == r:
      self.tree[node] = nums[l]
      return
    
    mid = (l + r) // 2 

    self.build(nums, node * 2, l, mid)
    self.build(nums, node * 2 + 1, mid + 1, r)

    self.tree[node] = (
      self.tree[node * 2]
      + self.tree[node * 2 + 1]
    )
  
  def query(self, node, l, r, ql, qr):
    if qr < l or ql > r:
      return 0
    
    if ql <= l and r <= qr:
      return self.tree[node]
    
    mid = (l + r) // 2 

    return (
      self.query(node * 2, l, mid, ql, qr)
      + self.query(node * 2 + 1, mid + 1, r, ql, qr)
    )
  
  def update(self, node, l, r, idx, val):
    if l == r:
      self.tree[node] = val 
      return 
    
    mid = (l + r) // 2 

    if idx <= mid:
      self.update(node * 2, l, mid, idx, val)
    else:
      self.update(node * 2 + 1, mid + 1, r, idx, val)
    
    self.tree[node] = (
      self.tree[node * 2]
      + self.tree[node*2 + 1]
    )