def lengthOfLongestSubstring(s):
  left = 0 
  seen = set()
  maxLen = 0 

  for right in range(len(s)):
    while s[right] in seen:
      seen.remove(s[left])
      left += 1 
    
    seen.add(s[right])
    maxLen = max(maxLen, right - left + 1)
  
  return maxLen

print(lengthOfLongestSubstring("abcabcbb"))