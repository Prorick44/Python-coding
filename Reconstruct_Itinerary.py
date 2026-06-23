from collections import defaultdict 

def findItinery(tickets):
  graph = defaultdict(list)
  tickets.sort(reverse=True)

  for src, dst in tickets:
    graph[src].append(dst) 
  
  result = []

  def dfs(airport):
    while graph[airport]:
      dfs(graph[airport].pop())

    result.append(airport)
  
  dfs("JFK")
  return result[::-1]

