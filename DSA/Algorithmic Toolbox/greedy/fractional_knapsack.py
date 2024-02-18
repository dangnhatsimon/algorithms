from sys import stdin


def optimal_value(capacity: int, weights: list[int], values: list[int]) -> int:
    max_value = 0
    # write your code here
    if capacity == 0:
        return 0
    
    # Create a list of tuples (value per weight, weight, value)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    # Sort items based on value per weight ratio in descending order
    items.sort(reverse=True, key = lambda x: x[0])
    
    for item in items:
        if capacity == 0:
            break
        # Take the fraction of the item that fits into the backpack
        fraction = min(item[1], capacity) / item[1]
        # Update the maximum value and remaining capacity
        max_value += fraction * item[2]
        capacity -= fraction * item[1]
    return max_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
