class MyQueue:
  def __init__(self):
    self.inputStack = []
    self.outputStack = []

  def push(self, x):
    self.inputStack.append(x)
  
  def pop(self):
    self.peek()
    return self.outputStack.pop()
  
  def peek(self):
    if not self.outputStack:
      while self.inputStack:
        self.outputStack.append(self.inputStack.pop())
    
    return self.outputStack[-1]

  def empty(self):
    return not self.inputStack and not self.outputStack