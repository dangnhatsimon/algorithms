#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg, zero, i = 0, 0, 0, 0
    while i < len(arr):
        if arr[i] > 0:
            pos += 1/len(arr)
        elif arr[i] < 0:
            neg += 1/len(arr)
        else:
            zero += 1/len(arr) 
        i += 1
    print(f"{pos:6f}")
    print(f"{neg:6f}")
    print(f"{zero:6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
