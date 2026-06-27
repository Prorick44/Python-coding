class Fenwick:
  def __init__(self, n):
    self.n = n 
    self.bit = [0] * (n + 2)
  
  def update(self, idx, delta):
    while idx <= self.n:
      self.bit[idx] += delta 
      idx += idx & (-idx) 
  
  def rangeUpdate(self, l, r, val):
    self.update(l, val)
    self.update(r + 1, -val)
  
  def pointQuery(self, idx):
    ans = 0 
    while idx > 0:
      ans += self.bit[idx]
      idx -= idx & (-idx)
    
    return ans 
  