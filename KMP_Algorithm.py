def kmpSearch(text, pattern):
  m = len(pattern)
  lps = [0] * m

  length = 0 
  i = 1 

  while i < m:
    if pattern[i] == pattern[length]:
      length += 1 
      lps[i] = length
      i += 1

    else:
      if length != 0:
        length = lps[length-1]
      else:
        lps[i] = 0 
        i += 1 

  i = j = 0 

  while i < len(text):
    if text[i] == pattern[j]:
      i += 1 
      j += 1

    if j == m:
      return i - j 

    elif i < len(text) and text[i] != pattern[j]:
      if j != 0:
        j = lps[j-1]
      else:
        i += 1 

  return -1 

print(kmpSearch("abcabcabcabababd"), "ababd") 
  