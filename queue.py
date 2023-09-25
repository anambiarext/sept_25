class Queue:
  def __init__(self):
    self.queue = []

  def check_null(self):
    return len(self.queue) == 0

  def enqueue(self, element):
    self.queue.append(element)
    
  def dequeue(self):
    if not self.check_null():
      return self.queue.pop(0)
    else:
      print("Empty Queue")

  def display(self):
    print(self.queue)
    

queue = Queue()
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.display()

queue.dequeue()
queue.display()

queue.dequeue()
queue.dequeue()

queue.dequeue()
