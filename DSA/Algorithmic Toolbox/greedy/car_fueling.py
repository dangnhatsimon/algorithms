from sys import stdin


def min_refills(distance: int, tank: int, stops: list[int]) -> int:
    # write your code here
    stops.append(distance)
    stops.insert(0,0)
    fill = 0
    remain_tank = tank
    for i in range(len(stops)-1):
        if tank < (stops[i+1] - stops[i]):
            return -1
        if remain_tank < (stops[i + 1] - stops[i]):
            remain_tank = tank
            fill += 1
        remain_tank -= stops[i+1] - stops[i]
    return fill



if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
