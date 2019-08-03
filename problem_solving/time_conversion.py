#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t = []
    for i in range(len(s)):
            t.append(s[i])
    if s[8] == "A":
        t.remove('A')
    elif s[8] == "P":
        t.remove("P")

    t.remove('M')
    t.remove(':')
    t.remove(':')
    save = list(map(str, t))
    save.pop(0)
    save.pop(0)
    r = list(map(str, t))
    r = "".join(r)
    amt = r
    r = int(r)
    r = r+120000
    ro = ["0", "0"]
    if s[8] == "A" and int(r) < 240000:
        ma = list(str(amt))
        ma = "".join(ma)
        r = ma
    if s[8] == "P" and int(r) >= 240000:
        mqa = list(str(amt))
        mqa = "".join(mqa)
        r = mqa

    if int(r) >= 240000:
        ro = ro+save
        ro = ''.join(ro)
        r = ro

    r = list(str(r))
    r.insert(2, ":")
    r.insert(5, ":")
    r = "".join(r)
    return r

    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

