# Uses python3
import sys

def gcd(a, b):
    current_gcd = 1
    if a > b:
      divisor = b
      dividend = a
    else:
      divisor = a
      dividend = b

    while dividend % divisor != 0:
      remainder = dividend%divisor
      dividend = divisor
      divisor = remainder

    return divisor

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
