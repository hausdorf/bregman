#!/usr/bin/python

import math

def KL1d(xi, yi):
    if xi == 0.0:
        return 0.0
    else:
        return xi * math.log(xi/yi)
    
def KL(x, y):
    return reduce(lambda s, p: s+KL1d(*p), zip(x,y), 0.0)

