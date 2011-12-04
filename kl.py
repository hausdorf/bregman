#!/usr/bin/python

import math

def KL1d(xi, yi):
    if xi == 0.0:
        return 0.0
    else:
        return xi * math.log(xi/yi) - xi + yi
    
def KL(x, y):
    return math.fsum(map(KL1d, x, y))

