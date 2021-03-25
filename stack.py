class Stack:
  def __init__(self):
    self.stack = []

  def add(self, data):
    self.stack.append(data)

  def pop(self):
    self.stack.pop()

  def peek(self):
    if len(self.stack) > 0:
      return self.stack[-1]

A = Stack()
A.add("mon")
A.add("tue")
A.add("wed")
print(A.peek())
A.pop()
print(A.peek())