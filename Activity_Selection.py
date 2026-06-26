def activity_selection(start, end):
  activities = sorted(zip(start, end), key=lambda x: x[1])
  count = 1 
  last_end = activities[0][1]

  for s, e in activities[1:]:
    if s >= last_end:
      count += 1
      last_end = e 

  return count 

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

print(activity_selection(start, end))