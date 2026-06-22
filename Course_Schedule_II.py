from collections import defaultdict 

def findOrder(numCourses, prerequisites):
  graph = defaultdict(list)
  
  for a, b in prerequisites:
    graph[a].append(b)
  
  visiting = set()
  visited = set()

  result = []

  def dfs(course):
    if course in visiting:
      return False
    
    if course in visited:
      return True 
    
    visiting.add(course)

    for pre in graph[course]:
      if not dfs(pre):
        return False 

    visiting.remove(course)
    visited.add(course)

    result.append(course)

    return True

  for course in range(numCourses):
    if not dfs(course):
      return []
    
  return result
  