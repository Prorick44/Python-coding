class MapSum:
  def __init__(self):
    self.map = {}
  
  def insert(self, key, val):
    self.map[key] = val
  
  def sum(self, prefix):
    answer = 0 

    for key, value in self.map.items():
      if key.startswith(prefix):
        answer += value 
    
    return answer 