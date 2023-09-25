class Stack:
  def __init__(self):
    self.stack = []

  def check_null(self):
    return len(self.stack) == 0

  def push(self, element):
    self.stack.append(element)
    
  def pop(self):
    if not self.check_null():
      return self.stack.pop()
    else:
      print("Empty Stack")

  def display(self):
    print(self.stack)
    

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.display()

stack.pop()
stack.pop()
stack.pop()
stack.display()

stack.pop()
