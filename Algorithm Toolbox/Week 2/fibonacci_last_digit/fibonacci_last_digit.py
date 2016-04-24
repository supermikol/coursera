# Uses python3
import sys

def get_fibonacci_last_digit(n):
  if n == 0:
    return 0
  fib_array = [0]*(n+1)
  fib_array[1] = 1
  for i in range(2,n+1):
    fib_array[i] = (fib_array[i-1] + fib_array[i-2]) % 10

  return fib_array[n]
    # write your code here
    # return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
