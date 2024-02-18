def optimal_summands(n: int) -> list[int]:
    summands = []
    # write your code here
    if n <= 2:
        summands.append(n)
    else:
        candy = 1
        while n > 0:
            if n - candy >= candy + 1:
                summands.append(candy)
                n -= candy
                candy += 1
            else:
                summands.append(n)
                break
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
