def addOperators(num, target):
  result = []

  def dfs(index, path, value, prev):
    if index == len(num):
      if value == target:
        result.append(path)
      
      return 
    
    for i in range(index, len(num)):
      if i > index and num[index] == "0":
        break 

      curr = int(num[index:i+1])
      if index == 0:
        dfs(i+1, str(curr), curr, curr)
      
      else:
        dfs(i+1, path+"+"+str(curr), value-curr, curr)
        dfs(i+1, path+"-"+str(curr), value-curr, -curr)
        dfs(i+1, path+"*"+str(curr), value-prev+prev*curr)
  
  dfs(0, "", 0, 0)
  return result