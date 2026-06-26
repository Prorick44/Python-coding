class LazySegmentTree:
  def __init__(self, nums):
    self.n = len(nums)

    self.tree = [0] * (4 * self.n)
    self.lazy = [0] * (4 * self.n)

    self.build(nums, 1, 0, self.n - 1)

  def build(self, nums, node, l, r):
    if l == r:
      self.tree[node] = nums[l]
      return 
    
    mid = (l + r) // 2 

    self.build(nums, node * 2, l, mid)
    self.build(nums, node * 2 + 1, mid + 1, r)

    self.tree[node] = (
      self.tree[node * 2] + self.tree[node * 2 + 1]
    )
  
  def propagate(self, node, l, r):
    if self.lazy[node] != 0:
      self.tree[node] += (
        (r - l + 1) * self.lazy[node]
      )

      if l != r:
        self.lazy[node * 2] += self.lazy[node]
        self.lazy[node * 2 + 1] += self.lazy[node]
      
      self.lazy[node] = 0 
      
