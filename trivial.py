#!/usr/bin/python

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
    
    delim = ','

    (center, radius) = trivial(KL, ((float(xi) for xi in line.split(delim)) for line in sys.stdin))

    print '%.40s... %f' % (center, radius)

    return None

# Test with:
# tail -n +2 set1.txt | python trivial.py
#
# For a random permutation do:
# tail -n +2 set1.txt | sort -R | python trivial.py
if __name__ == '__main__':
    main(sys.argv)
