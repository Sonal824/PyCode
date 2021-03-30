#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    lengthOfS = len(s);
    numberOfAs = 0;
    countAs = countAsFromString(s);
    numberOfAs += countAs * (n // lengthOfS);
    remaningsubstring = n % lengthOfS;
    numberOfAs += countAsFromString(s[0:remaningsubstring]);
    return numberOfAs;

def countAsFromString(s):
    count = 0;
    for i in s:
        if i == 'a':
            count += 1
    return count;
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
