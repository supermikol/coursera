# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        storage = [0 for x in range(self.n)]
        for vertex in range(self.n):
                # print "starting for:", vertex
                height = 0
                i = vertex
                while i != -1:
                    if storage[i] != 0:
                        height += storage[i]
                        # print "found %d in storage, adding %d" % (i, storage[i])
                        # print "height now:", height
                        i = -1
                    else:
                        height += 1
                        # print "adding 1, height now:",height
                        # print "assigning %d to %d" % (self.parent[i], i)
                        i = self.parent[i]
                j = vertex
                temp_height = height
                while storage[j] == 0:
                    if j == -1:
                        break
                    # print "storing %d in %d" % (temp_height, j)
                    storage[j] = temp_height
                    temp_height -=  1
                    j = self.parent[j]
                # print "Final:",vertex,storage
                maxHeight = max(maxHeight, height);
        return maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
