def restoreTpAddresses(s):
  result = []

  def backtrack(index, dots, current):
    if dots == 4 and index == len(s):
      result.append(current[:-1])
      return
    
    if dots > 4:
      return 
    
    for j in range(index, min(index+3, len(s))):
      if int(s[index:j+1]) < 256 and (index == j or s[index] != '0'):
        backtrack(j+1, dots+1, current+s[index:j+1]+'.')
  
  backtrack(0, 0, "")
  return result