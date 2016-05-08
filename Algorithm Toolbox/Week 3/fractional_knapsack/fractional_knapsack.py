# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    # write your code here
    limit = capacity
    n = len(weights)
    weighted_values = sorted([[v/w, w] for v,w in zip(values,weights)], key = lambda l:l[0], reverse = True)
    i = 0
    value = 0
    while limit > 0 and i < n:
      a = min(weighted_values[i][1],limit)
      value += a * weighted_values[i][0]
      limit -= a
      i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
