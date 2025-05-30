#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

def staircase(n):
    for i in range(n):
        str = ""
        for j in range(n):
            if n - j > i + 1:
                str += " "
            else:
                str += "#"
        print(str)

staircase(4)
staircase(5)
staircase(6)
staircase(7)
