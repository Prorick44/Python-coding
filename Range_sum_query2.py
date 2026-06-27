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
  