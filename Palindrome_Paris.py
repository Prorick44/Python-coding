def palindromePairs(words):
  lookup = {w[::-1]: i for i, w in enumerate(words)}
  result = []

  for i, word in enumerate(words):
    for j in range(len(word) + 1):
      prefix = word[:j]
      suffix = word[j:]

      if prefix == prefix[::-1]:
        if suffix in lookup and lookup[suffix] != i:
          result.append([lookup[suffix], i])
      
      if j != len(word) and suffix == suffix[::-1]:
        if prefix in lookup and lookup[prefix] != i:
          result.append([i, lookup[prefix]])
  
  return result