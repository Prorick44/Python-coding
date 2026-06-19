def longestWord(words):
  words.sort()

  valid = {""}
  answer = ""

  for word in words:
    if word[:-1] in valid:
      valid.add(word)
      if len(word) > len(answer):
        answer = word 
  
  return answer 