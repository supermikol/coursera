# Uses python3
import sys

def get_change(n):
    #write your code here
    count = 0
    while n > 0:
      if (n >= 10):
        n -= 10
      elif (n >= 5):
        n -= 5
      else:
        n -= 1
      count += 1
    return count

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
