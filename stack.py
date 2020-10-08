class Stack:
  def __init__(self, size):
    self._size = size
    self._arr = []
    self._head = -1

  def isFull(self):
    return len(self._arr) == self._size
  def isEmpty(self):
    return self._head == -1

  def push(self, value):
      if not self.isFull():
          self._arr.append(value)
          self._head += 1
      else:
          print("\nSTACK FULL\n")

  def pop(self):
      if not self.isEmpty():
          self._arr = self._arr[:-1]
          self._head -= 1
      else:
          print("\nSTACK EMPTY\n")

  def peek(self):
      return self._arr[-1] if not self.isEmpty() else "STACK EMPTY"

  def printStack(self):
      for val in self._arr:
          print(val, end=' ')
      print("\n")

def main():
    ask = int(input("Length of stack: "))
    stack = Stack(ask)
    for i in range(10):
        stack.push(i)
    stack.pop()
    stack.printStack()
    print(stack.peek())

if __name__  == "__main__":
    main()
