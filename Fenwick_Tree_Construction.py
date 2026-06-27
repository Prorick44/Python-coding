class FenwickTree:
  def __init__(self, n):
    self.n = n 
    self.bit = [0] * (n + 1)

  def update(self, i, delta):
    while i <= self.n:
      self.bit[i] += delta 
      i += i & (-i)

ft = FenwickTree(5)
ft.update(1, 2)
ft.update(2, 3)
ft.update(3, 5)

print(ft.bit)
