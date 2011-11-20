#/usr/bin/python

import sys
import math

from kl import KL

def trivial(dist, it):
    curcenter = None
    radius = 0

    for vec in it:
        if not curcenter:
            curcenter = [xi for xi in vec]

        radius = max(radius, dist([xi for xi in vec], curcenter))

    return (curcenter, radius)

def main(argv):
    
    delim = None

    (center, radius) = trivial(KL, ((float(xi) for xi in line.split(delim)) for line in sys.stdin))

    print center, radius

    return None

if __name__ == '__main__':
    main(sys.argv)
