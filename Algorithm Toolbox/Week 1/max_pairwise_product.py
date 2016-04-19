# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

if a[0] > a[1]:
  max_val = a[0]
  second_val = a[1]
else:
  max_val = a[1]
  second_val = a[0]

for i in range(2,n):
  if a[i] > second_val:
    if a[i] > max_val:
      second_val = max_val
      max_val = a[i]
    else:
      second_val = a[i]

print(max_val * second_val)