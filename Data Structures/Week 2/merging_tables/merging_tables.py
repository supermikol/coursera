# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source) #returns root

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size
    global ans
    # print("answer is", ans)
    if rank[realDestination] < rank[realSource]:
        lines[realSource] += lines[realDestination]
        parent[realDestination] = realSource
        if lines[realSource] > ans:
            ans = lines[realSource]
    else:
        lines[realDestination] += lines[realSource]
        parent[realSource] = realDestination
        if lines[realDestination] > ans:
            ans = lines[realDestination]
        if rank[realSource] == rank[realDestination]:
            rank[realDestination] += 1

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

