from collections import defaultdict, OrderedDict 

class LFUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.minFreq = 0 
    self.keyToValFreq = {}
    self.freqToKeys = defaultdict(OrderedDict)
  
  def update(self, key):
    value, freq = self.keyToValFreq[key]
    del self.freqToKeys[freq][key]
    if not self.freqToKeys[freq]:
      del self.freqToKeys[freq]
      if self.minFreq == freq:
        self.minFreq += 1
    
    self.freqToKeys[freq + 1][key] = None 
    self.keyToFreq[key] = (value, freq + 1)
  
  def get(self, key):
    if key not in self.keyToValFreq:
      return -1 
    
    value, _ = self.keyToValFreq[key]
    self.update(key)
    return value 
  
  def put(self, key, value):
    if self.capacity == 0:
      return 
    
    if key in self.keyToValFreq:
      _, freq = self.keyToValFreq[key]
      self.keyToValFreq[key] = (value, freq)
      self.update(key)
      return 

    if len(self.keyToValFreq) == self.capacity:
      oldKey, _ = self.freqToKeys[self.minFreq].popitem(last=False)
      del self.keyToValFreq[oldKey]

      if not self.freqToKeys[self.minFreq]:
        del self.freqToKeys[self.minFreq]
    
    self.keyToValFreq[key] = (value, 1)
    self.freqToKeys[1][key] = None 
    self.minFreq = 1 