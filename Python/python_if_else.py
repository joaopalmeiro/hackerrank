#!/bin/python3

import math
import os
import random
import re
import sys


def weird_or_not_weird(n):
    if(n % 2 == 0):
        if(n <= 5 or n > 20):
            return("Not Weird")
        else:
            return("Weird")
    else:
        return("Weird")


if __name__ == '__main__':
    n = int(input().strip())

    print(weird_or_not_weird(n))
