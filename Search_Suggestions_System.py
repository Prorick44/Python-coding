def suggestedProducts(products, searchWord):
  products.sort()

  answer = []
  prefix = ""

  for ch in searchWord:
    prefix += ch 
    suggestions = []
    for product in products:
      if product.startswith(prefix):
        suggestions.append(product)
        if len(suggestions) == 3:
          break 
    
    answer.append(suggestions)
  
  return answer 