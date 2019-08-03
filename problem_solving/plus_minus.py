#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    a=len(arr)
    z=0
    n=0
    p=0
    for i in range(a):
        if arr[i]>0:
            p=p+1

        if arr[i]<0:
            n=n+1

        if arr[i]==0:
            z=z+1
    print(p/a)
    print(n/a)
    print(z/a)








if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
