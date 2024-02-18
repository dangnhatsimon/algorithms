from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments: Segment) -> list[int]:
    points = []
    # write your code here
    segments.sort(key = lambda seg: seg[1])
    i = 0
    while i != len(segments):
        point = segments[i][1]
        while i != len(segments) and point >= segments[i][0]:
            i += 1
        points.append(point)
        
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
