class Codec:
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  def encodeId(self, num):
    s = ""
    while num:
      s += self.chars[num % 62]
      num //= 62
    return s[::-1]
  
def decodeId(code):
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  mp = {c: i for i, c in enumerate(chars)}
  num = 0 
  for c in code:
    num = num * 62 + mp[c]
  return num