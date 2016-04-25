# Uses python3
def calc_fib(n):
  if n == 0:
    return 0
  fib_array = [0]*(n+1)
  fib_array[1] = 1
  for i in range(2,n+1):
    fib_array[i] = fib_array[i-1] + fib_array[i-2]

  return fib_array[n]

n = int(input())
print(calc_fib(n))
