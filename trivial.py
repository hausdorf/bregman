#/usr/bin/python

import sys
import math

def KL1d(xi, yi):
    if xi == 0.0:
        return 0.0
    else:
        return xi * math.log(xi/yi)

def KL(x, y):
    return reduce(lambda s, p: s+KL1d(p[0], p[1]), zip(x,y), 0.0)

def trivial(dist, it):
    curcenter = None
    radius = 0

    for vec in it:
        if not curcenter:
            curcenter = vec

        radius = max(radius, dist(vec, curcenter))

    return (curcenter, radius)

def main(argv):
    
    delim = None

    (center, radius) = trivial(KL, (map(float, line.split(delim)) for line in sys.stdin))

    print center, radius

    return None

if __name__ == '__main__':
    main(sys.argv)
