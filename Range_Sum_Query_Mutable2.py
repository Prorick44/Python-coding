class FenwickTree:
  def __init__(self, n):
    self.n = n 
    self.bit = [0] * (n + 1)
  
  def update(self, i, delta):
    while i <= self.n:
      self.bit[i] += delta 
      i += i & (-i)
    
  def query(self, i):
    ans = 0 

    while i > 0:
      ans += self.bit[i]
      i -= i &(-i)
    
    return ans 
  
  def rangeQuery(self, l, r):
    return self.query(r) - self.query(l - 1)
  
class NumArray:
  def  __init__(self, nums):
    self.arr = nums[:]
    self.ft = FenwickTree(len(nums))
    for i, x in enumerate(nums):
      self.ft.update(i + 1, x)
  
  def update(self, index, val):
    delta = val - self.arr[index]
    self.arr[index] = val 
    self.ft.update(index+1, delta)
  
  def sumRange(self, left, right):
    return (
      self.ft.query(right + 1)
      - self.ft.query(left)
    )