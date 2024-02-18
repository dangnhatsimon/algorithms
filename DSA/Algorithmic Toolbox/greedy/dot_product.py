from itertools import permutations


# def max_dot_product(first_sequence, second_sequence):
#     max_product = 0
#     for permutation in permutations(second_sequence):
#         dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
#         max_product = max(max_product, dot_product)

#     return max_product

def max_dot_product(first_sequence: list[int], second_sequence: list[int]) -> int:
    max_product = 0
    length = len(first_sequence)
    for i in range(length):
        max_product += max(first_sequence) * max(second_sequence)
        first_sequence.remove(max(first_sequence))
        second_sequence.remove(max(second_sequence))
    return max_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
