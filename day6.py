#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    # DP Solution
    if n == 1: return 1;
    elif n == 2: return 2;
    elif n ==3: return 4;
    arr = {};
    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 4;
    for i in range(3,n):
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1];
    return arr[n-1];

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
