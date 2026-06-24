def numDecodings(s):
  dp1 = 1 
  dp2 = 0 if s[-1] == "0" else 1 

  for i in range(len(s)-2, -1, -1):
    curr = 0 
    if s[i] != "0":
      curr = dp2 

      if int(s[i:i+2]) <= 26:
        curr += dp1 
    
    dp1 = dp2 
    dp2 = curr 
  
  return dp2 

print(numDecodings("226"))
