# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def Swap(self, i, j):
      # self._swaps.append((i,j))
      temp = self.heap_index[i]
      self.heap_index[i] = self.heap_index[j]
      self.heap_index[j] = temp

    def LeftChild(self, i):
      return 2*i + 1

    def RightChild(self, i):
      return 2*i + 2

    def SiftDown(self, i):
      minIndex = i
      l = 2*i + 1
      r = 2*i + 2
      minTemp = i
      if r <= self.num_workers - 1:
        if self.threads[self.heap_index[l]] < self.threads[self.heap_index[r]]:
          minTemp = l
        elif self.threads[self.heap_index[r]] < self.threads[self.heap_index[l]]:
          minTemp = r
        else:
          minTemp = l if self.heap_index[l] < self.heap_index[r] else r
      elif l <= self.num_workers - 1:
        minTemp = l

      if minTemp != i:
        if self.threads[self.heap_index[minTemp]] < self.threads[self.heap_index[minIndex]]:
          minIndex = minTemp
        elif self.threads[self.heap_index[minTemp]] == self.threads[self.heap_index[minIndex]]:
          minIndex = minIndex if self.heap_index[minIndex] < self.heap_index[minTemp] else minTemp

      if i != minIndex:
        self.Swap(i, minIndex)
        self.SiftDown(minIndex)

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        self.threads = [0] * self.num_workers
        self.heap_index = list(range(self.num_workers))

        for i in range(len(self.jobs)):
          self.assigned_workers[i] = self.heap_index[0]
          self.start_times[i] = self.threads[self.heap_index[0]]
          self.threads[self.heap_index[0]] += self.jobs[i]
          self.SiftDown(0)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

