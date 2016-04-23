# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def Swap(self, i, j):
    self._swaps.append((i,j))
    temp = self._data[i]
    self._data[i] = self._data[j]
    self._data[j] = temp

  def LeftChild(self, i):
    return 2*i + 1

  def RightChild(self, i):
    return 2*i + 2

  def SiftDown(self, i):
    maxIndex = i
    l = self.LeftChild(i)
    if l <= len(self._data) - 1 and self._data[l] < self._data[maxIndex]:
      maxIndex = l
    r = self.RightChild(i)
    if r <= len(self._data) -1 and self._data[r] < self._data[maxIndex]:
      maxIndex = r
    if i != maxIndex:
      self.Swap(i, maxIndex)
      self.SiftDown(maxIndex)

  def GenerateSwaps(self):
    # The following naive implementation just sorts
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap,
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(int(len(self._data)/2))[-1::-1]:
      self.SiftDown(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
