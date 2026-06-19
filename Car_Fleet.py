def carFleet(target, position, speed):
  cars = sorted(zip(position, speed), reverse = True)
  stack = []
  for pos, spd in cars:
    time = (target - pos) / spd 
    stack.append(time)
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
      stack.pop()
  
  return len(stack)

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))