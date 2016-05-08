# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=lambda x: x.start)
    endPointer = segments[0].end
    for s in segments:
        if s.start <= endPointer:
            endPointer = min(endPointer,s.end)
        else:
            points.append(endPointer)
            endPointer = s.end
    points.append(endPointer)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
