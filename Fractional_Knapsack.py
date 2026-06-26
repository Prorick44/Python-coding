def fractional_knapsack(capacity, items):
  items.sort(key=lambda x: x[0]/x[1], reverse=True)

  total = 0

  for value, weight in items:
    if capacity >= weight:
      total += value 
      capacity -= weight 
    else:
      total += value * (capacity / weight)
      break 
  
  return total 

items = [(60, 10), (100, 20), (120, 30)]
print(fractional_knapsack(50, items))
