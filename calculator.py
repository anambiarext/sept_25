import math

class Calculator:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def add(self):
    return self.a + self.b

  def sub(self):
    return self.a - self.b
    
  def prod(self):
    return self.a * self.b
    
  def div(self):
    return self.a / self.b

number_1 = int(input("Enter 1st Number : "))
number_2 = int(input("Enter 2nd Number : "))
calci = Calculator(number_1, number_2)
print(calci.add())
print(calci.sub())
print(calci.prod())
print(calci.div())
