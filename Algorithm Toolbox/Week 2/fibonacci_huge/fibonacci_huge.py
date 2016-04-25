# Uses python3
import sys

def get_fibonaccihuge(n, m):
    # write your code here
  if n == 0:
    return 0
  pis_array = [0]*(min(6*m,n+1))
  pis_array[1] = 1
  index = 0

  #can strictly calculate the pisano sequence WITHOUT the fibonacci sequence!
  #Recall that fib[i] % m = (fib[i-1] + fib[i-2]) % m
  for i in range(2,min(6*m,n+1)):
    pis_array[i] = (pis_array[i-1] + pis_array[i-2]) % m
    if pis_array[i] == 1 and pis_array[i-1] == 0:
      index = i-1
      break
  if m > n:
    return pis_array[n]
  return pis_array[(n % index)]



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
