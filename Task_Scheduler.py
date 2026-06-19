from collections import Counter 

def leastInterval(tasks, n):
  freq = Counter(tasks)
  maxFreq = max(freq.values())
  maxCount = list(freq.values()).count(maxFreq)
  return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)

print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))