def rabinKarp(text, pattern):
  d = 256
  q = 101 

  n = len(text)
  m = len(pattern)

  h = pow(d, m-1) % q 

  p = t = 0 

  for i in range(m):
    p = (d*p + ord(pattern[i])) % q 
    t = (d*t + ord(text[i])) % q 

  for i in range(n-m+1):
    if p == t:
      if text[i:i+m] == pattern:
        return i 
      
    if i < n-m:
      t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q 

      if t < 0:
        t += q 
  
  return -1 

print(rabinKarp("GEEKS FOR GEEKS", "FOR"))