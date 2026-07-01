class Codec:
  def __init__(self):
    self.id = 0 
    self.shortToLong = {}
    self.longToShort = {}
  
  def encode(self, longUrl):
    if longUrl in self.longToShort:
      return self.longToShort[longUrl]
    
    self.id += 1 
    short = "http://tinyurl.com/" + str(self.id)
    self.shortToLong[short] = longUrl 
    self.longToShort[longUrl] = short 
    return short
  
  def decode(self, shortUrl):
    return self.shortToLong[shortUrl]
  

codec = Codec()

short = codec.encode(
  "https://google.com"
)
print(short)
print(codec.decode(short))