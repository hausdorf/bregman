#!/usr/bin/python

import math

def KLgradinv(X):
    return map(math.exp, X)

def KLgrad(x):
    return map(math.log, x)

def KL1d(xi, yi):
    return xi * math.log(xi/yi) - xi + yi
    
def KL(x, y):
    return math.fsum(map(KL1d, x, y))

