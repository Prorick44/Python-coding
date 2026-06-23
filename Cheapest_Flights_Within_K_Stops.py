from collections import defaultdict, deque 

def findCheapestPrice(n, flights, src, dst, k):
  graph = defaultdict(list)

  for u, v, price in flights:
    graph[u].append((v, price))
  
  queue = deque([(src, 0)])
  prices = [float('inf')] * n 
  prices[src] = 0 
  stops = 0 

  while queue and stops <= k:
    size = len(queue)
    tempPrices = prices.copy()
    for _ in range(size):
      city, cost = queue.popleft()
      for nei, price in graph[city]:
        if cost + price < tempPrices[nei]:
          tempPrices[nei] = cost + price 
          queue.append((nei, cost + price))

    prices = tempPrices
    stops += 1 

  return prices[dst] if prices[dst] != float('inf') else 1 
 