#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    al=0
    bo=0
    for i in range(len(a)):
        if a[i]>b[i]:
            al=al+1
            result=[al,bo]
        elif a[i]<b[i]:
            bo=bo+1
            result=[al,bo]
        elif a[i]==b[i]:
            bo=bo+0
            al=al+0
        i=i+1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
