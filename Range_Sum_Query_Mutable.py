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

    self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

  def update(self, node, start, end, index, value):
    if start == end:
      self.tree[node] = value
      return

    mid = (start + end) // 2

    if index <= mid:
      self.update(node * 2, start, mid, index, value)
    else:
      self.update(node * 2 + 1, mid + 1, end, index, value)

    self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

class NumArray:
  def __init__(self, nums):
    self.seg = SegmentTree(nums)

  def update(self, index, val):
    self.seg.update(
      1,
      0,
      self.seg.n - 1,
      index, 
      val
    )
  
  def sumRange(self, left, right):
    return self.seg.query(
      1, 
      0,
      self.seg.n - 1,
      left, 
      right 
    )