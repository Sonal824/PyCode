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


# Complete the stepPerms function below.
# cacheRes = dict()
# cacheRes[1] = 1
# cacheRes[2] = 2
# cacheRes[3] = 4
# def stepPerms(n):
#     # Recursive Solution
#     if n==0: return 0;
#     if n in cacheRes.keys(): return cacheRes[n]
#     cacheRes[n]= stepPerms(n-3) + stepPerms(n-2) + stepPerms(n-1)
#     return cacheRes[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
