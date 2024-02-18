from itertools import permutations


def largest_number_naive(numbers) -> int:
    # numbers = list(map(str, numbers))

    # largest = 0

    # for permutation in permutations(numbers):
    #     largest = max(largest, int("".join(permutation)))

    numbers = [str(num) for num in numbers]
    
    # Sort the numbers based on custom comparator
    numbers.sort(key = lambda x: x * 3, reverse=True)
    # The key function ensures that numbers are compared as strings, and the *3 ensures proper comparison for numbers with different lengths
    
    # Concatenate the sorted numbers and return the result
    largest = ''.join(numbers)
    
    return largest
    


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
