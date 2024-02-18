#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal_right, diagonal_left, i, j = 0, 0, 0, len(arr) - 1 
    while i <= len(arr) and j >= 0:
        diagonal_right += arr[i][i]
        diagonal_left += arr[i][j]
        i += 1
        j -= 1
    return abs(diagonal_right - diagonal_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
