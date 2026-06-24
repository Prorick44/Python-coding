import bisect 

def lengthOfLIS(nums):
  lis = []
  for num in nums:
    pos = bisect.bisect_left(lis, num)
    if pos == len(lis):
      lis.append(num)
    else:
      lis[pos] = num 
  
  return len(lis)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
