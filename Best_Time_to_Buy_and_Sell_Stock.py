def maxProfit(prices):
  buy = prices[0]
  profit = 0 

  for price in prices:
    buy = min(buy, price)
    profit = max(profit, price - buy)
  
  return profit 

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
