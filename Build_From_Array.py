class FenwickTree:
  def __init__(self, nums):
    self.n = len(nums)
    self.bit = [0] * (self.n + 1)

    for i in range(self.n):
      self.update(i + 1, nums[i])
  
  def update(self, i, delta):
    while i <= self.n:
      self.bit[i] += delta 
      i += i & (-i)
  
  def query(self, i):
    ans = 0 
    while i > 0:
      ans += self.bit[i]
      i -= i & (-i)
    
    return ans 
  