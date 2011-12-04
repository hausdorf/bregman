#!/usr/bin/python

import sys
import math
import argparse

from kl import KL

def trivial(div, it):
    center = None
    radius = 0.0

    for v in it:
        vec = list(v)
        if not center:
            center = vec
        else:
            radius = max(radius, div(vec, center))

    return (center, radius)

def main(argv):
    
    parser = argparse.ArgumentParser(description='Run Nielsen & Nock algorithm for right balls on standard input')
    parser.add_argument('-d', '--delimiter', nargs='?', default=',', dest='delim')
    args = parser.parse_args()
                
    (center, radius) = trivial(KL, (map(float, line.split(args.delim)) for line in sys.stdin))

    print '%.40s... %f' % (center, radius)

    return None

# Test with:
# tail -n +2 set1.txt | python trivial.py
#
# For a random permutation do:
# tail -n +2 set1.txt | sort -R | python trivial.py
if __name__ == '__main__':
    main(sys.argv)
