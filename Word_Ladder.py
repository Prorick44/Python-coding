from collections import defaultdict, deque 

def ladderLength(beginWord, endWord, wordList):
  if endWord not in wordList:
    return 0
  
  neighbors = defaultdict(list)
  wordList.append(beginWord)
  for word in wordList:
    for i in range(len(word)):
      pattern = word[:i] + "*" + word[i+1:]
      neighbors[pattern].append(word)
  
  queue = deque([beginWord])
  visited = {beginWord}
  level = 1 
  while queue:
    for _ in range(len(queue)):
      word = queue.popleft()
      if word == endWord:
        return level 
      
      for i in range(len(word)):
        pattern = word[:i] + "*" + word[i+1:]

        for nei in neighbors[pattern]:
          if nei not in visited:
            visited.add(nei)
            queue.append(nei)

    level += 1 
    
  return 0