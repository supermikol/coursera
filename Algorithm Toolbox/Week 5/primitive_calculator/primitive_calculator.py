# Uses python3
import sys

def optimal_sequence(n):
    val = [0] * (n + 1)
    for i in range(2,n+1):
        div_three = float("inf")
        div_two = float("inf")
        if i % 3 == 0:
            div_three = val[i//3] + 1
        if i % 2 == 0:
            div_two = val[i//2] + 1
        plus_one = val[i-1] + 1
        val[i] = min(div_three, div_two, plus_one)
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and val[n] - 1 == val[n//3]:
            n = n // 3
        elif n % 2 == 0 and val[n] - 1 == val[n//2]:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
