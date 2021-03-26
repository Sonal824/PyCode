#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    hashtable = []; #to check uniqueness of number
    returncount = 0; # to store and return the data
    for i in ar:
        if (not i in hashtable):
            hashtable.append(i)
            totalcount = 0
            for j in ar:
                if(i == j):
                    totalcount = totalcount + 1
            if(totalcount > 1):
                returncount += totalcount // 2;
    return returncount;  
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()