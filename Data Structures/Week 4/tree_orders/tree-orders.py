# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

    self.inOrderResult = []
    self.preOrderResult = []
    self.postOrderResult = []
    self.traverse(0)

  def traverse(self, index):
    self.preOrderResult.append(self.key[index])
    if self.left[index] != -1:
      self.traverse(self.left[index])
    self.inOrderResult.append(self.key[index])
    if self.right[index] != -1:
      self.traverse(self.right[index])
    self.postOrderResult.append(self.key[index])

  def inOrder(self):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.inOrderResult

  def preOrder(self):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.preOrderResult

  def postOrder(self):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.postOrderResult

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
