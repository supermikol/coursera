# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    #0 index for each piece(0 = first piece), 1-index for weights (1 = knapsack of 1)
    values = [[0] * (W+1) for i in w]
    # print(values)
    for x in range(len(w)): #x = piece
      # print("x:",x)
      for i in range(1,W+1): #i = weight
        values[x][i] = values[x-1][i]
        val = 0
        if i >= w[x]:
          val = values[x-1][i-w[x]] + w[x]
        if val > values[x][i]:
            values[x][i] = val
      # print(values)
    return values[len(w)-1][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
