## Plus Minus

import math
import os
import random
import re
import sys


def plusMinus(arr):
    n = len(arr)
    pcnt, ncnt, zcnt = 0, 0, 0

    for i in arr:
        if i > 0:
            pcnt += 1
        elif i < 0:
            ncnt += 1
        else:
            zcnt += 1

    print("%.6f" % (pcnt / n))
    print("%.6f" % (ncnt / n))
    print("%.6f" % (zcnt / n))


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
