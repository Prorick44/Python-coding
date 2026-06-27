class FenwickTree:
  def __init__(self, n):
    self.n = n 
    self.bit = [0] * (n + 1)
  
  def update(self, idx, delta):
    while idx <= self.n:
      self.bit[idx] += delta 
      idx += idx & (-idx)
  
  def query(self, idx):
    ans = 0 

    while idx > 0:
      ans += self.bit[idx]
      idx -= idx & (-idx)
    
    return ans 
  
  def rangeQuery(self, l, r):
    return (
      self.query(r)
      - self.query(l - 1)
    )
  