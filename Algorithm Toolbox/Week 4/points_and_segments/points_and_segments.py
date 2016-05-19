# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    max_val = max(ends)
    counter = [0] * (max_val + 1)
    print(max(ends))
    for i in range(len(starts)):
        for j in range(starts[i],ends[i]+1):
            print(j)
            counter[j] += 1
    for i in range(len(points)):
        if points[i] <= max_val:
            cnt[i] = counter[points[i]]
            print("cnt",i,"=",cnt[i])
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # print(starts,ends,points)
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
