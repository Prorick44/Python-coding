from math import gcd 

class SegmentTree:
  def __init__(self, nums):
    self.n = len(nums)
    self.tree = [0] * (4 * self.n)
    self.build(nums, 1, 0, self.n - 1)
  
  def build(self, nums, node, start, end):
    if start == end:
      self.tree[node] = nums[start]
      return 
    
    mid = (start + end) // 2 

    self.build(nums, node * 2, start, mid)
    self.build(nums, node * 2 + 1, mid + 1, end)

    self.tree[node] = gcd(self.tree[node * 2], self.tree[node * 2 + 1])