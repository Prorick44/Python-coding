def maxProfit(prices):
  sell = 0 
  hold = float('-inf')
  cooldown = 0 

  for price in prices:
    prevSell = sell 
    sell = hold + price 
    hold = max(hold, cooldown-price)
    cooldown = max(cooldown, prevSell)
  
  return max(sell, cooldown)

print(maxProfit([1,2,3,0,2]))
