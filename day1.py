#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    lookuplist = [];
    pairs = 0;
    for i in ar:
        if(not i in lookuplist):
            lookuplist.append(i)
        else:
            pairs += 1
            lookuplist.remove(i)
    return pairs;  
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()