class Cell:
  def __init__(self):
    self.value = 0
    self.formula = None 
    self.parents = {}
    self.children = set()

from collections import defaultdict 

class Excel:
  def __init__(self):
    self.sheet = defaultdict(int)
  
  def set(self, r, c, v):
    self.sheet[(r, c)] = v 
  
  def get(self, r, c, cells):
    ans = 0

    for x in cells:
      ans += self.sheet[x]

    self.sheet[(r, c)] = ans 

    return ans 
