def decodeString(s):
  stack = []
  currentString = ""
  currentNum = 0 

  for ch in s:
    if ch.isdigit():
      currentNum = currentNum * 10 + int(ch)
    elif ch == '[':
      stack.append((currentString, currentNum))
      currentString = ""
      currentNum = 0 
    elif ch == ']':
      prevString, num = stack.pop()
      currentString = prevString + num * currentString 
    else:
      currentString += ch 
  
  return currentString