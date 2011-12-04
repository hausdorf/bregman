#!/usr/bin/python

import sys
import random
import argparse

from kl import KL

# Smallest Enclosing Right Ball (Nielsen & Nock approx)
# div must be convex in both arguments
# dataiter is an iterator over the data points
# T is the number of iterations to run
def SERB(div, dataiter, T):
    data = tuple(dataiter)

    center = random.choice(data)
    for t in range(1, T):
        s = max(data, key = lambda x: div(x, center))
        radius = div(s, center)
        center = map(lambda x, y: (x + t*y)/(t+1), s, center)

    return (center, max(map(lambda x: div(x, center), data)))

def main(argv):
    
    parser = argparse.ArgumentParser(description='Run Nielsen & Nock algorithm for right balls on standard input')
    parser.add_argument('-d', '--delimiter', nargs='?', default=',', dest='delim')
    parser.add_argument('-T', '--iterations', nargs='?', type=int, default=100, dest='iterations')
    args = parser.parse_args()

    (center, radius) = SERB(KL, (tuple(float(xi) for xi in line.split(args.delim)) for line in sys.stdin), args.iterations)
    
    print '%.40s... %f' % (center, radius)

    return None

# Test with:
# tail -n +2 set1.txt | python nielsen_nock.py
#
# For a random permutation do:
# tail -n +2 set1.txt | sort -R | python nielsen_nock.py
if __name__ == '__main__':
    main(sys.argv)
