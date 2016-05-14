# Uses python3
import sys


def binary_search_wrapper(a,x):
    left, right = 0, len(a)
    if len(a) == 0:
        return -1
    mid = len(a)//2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, 0, mid-1)
    else:
        return binary_search(a, x, mid+1, len(a)-1)

def binary_search(a, x, l, r):
    # write your code here
    if l>r:
        return -1
    mid = l + (r-l)//2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, l, mid-1)
    else:
        return binary_search(a, x, mid+1, len(a)-1)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search_wrapper(a, x), end = ' ')
