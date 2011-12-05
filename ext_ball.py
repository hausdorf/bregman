from math import log, exp, e
from scipy.optimize import brentq
from kl import KL, KLgrad, KLgradinv
import argparse
import sys

#SET1 = 'set1.txt'
#BAD1 = 'bad.txt'
#GOOD = 'good.txt'

def lerp(p1, p2, lamb):
    return [(1-lamb) * p1_i + lamb * p2_i for p1_i, p2_i in zip(p1, p2)];

def grad_lerp(p, c, lamb):
    g_p = KLgrad(p)
    g_c = KLgrad(c)
    x_l = KLgradinv(lerp(g_p, g_c, lamb))
    return x_l

def new_center(l_c, x_far, p, c):
    x_c = grad_lerp(p, c, l_c)
    return KL(x_far, x_c) - KL(p, x_c)

def midpoint(l, p, c):
	x_l = grad_lerp(p, c, l)
	return KL(c, x_l) - KL(p, x_l)

def ball_isect(l, p1, p2, r):
	return KL(grad_lerp(p1, p2, l), p2) - r

# meb_kl : point c -> radius r -> point p -> point p_far
# each point c, p, and p_far are d-dimensional
def meb_kl(c, r, p):

    # Find the point opposite p
    l_far = brentq(ball_isect, 1, 300, args=(p, c, r))
    #print KL(grad_lerp(p, c, l_far), c)

    # Find the midpoint between the far point and p
    x_far = grad_lerp(p, c, l_far)
    l_c = brentq(new_center, 0, l_far, args=(x_far, p, c))
    #print KL(grad_lerp(p, c, l_far), grad_lerp(p, c, l_c)), KL(p, grad_lerp(p, c, l_c))
    
    return l_c

#def set1_meb_kl():
#	f = open(GOOD)
#
#	# get dimensions and num of examples
#	dim,n = map(int, f.readline().split(','))
#	S = [map(float, l.split(',')) for l in f.readlines()]
#
#	c = S[0]
#	p = S[1]
#	mid = grad_lerp(p, c, brentq(midpoint, 0, 1, args=(p, c)))
#	r = KL(p, mid)
#	c = mid
#	for i in range(2, n):
#		p = S[i]
#
#		if KL(p, c) < r:
#			continue
#
#		l_c = meb_kl(c, r, p)
#		c = grad_lerp(p, c, l_c)
#		r = KL(p, c)
#		print c, r
#
#	f.close()

def streamMEB(it):
    c = it.next()
    p = it.next()

    c = grad_lerp(p, c, brentq(midpoint, 0, 1, args=(p, c)))
    r = KL(p, c)

    for p in it:
        if KL(p, c) < r:
            continue

        l_c = meb_kl(c, r, p)
        c = grad_lerp(p, c, l_c)
        r = KL(p, c)
        
    return (c, r)

def main():
    parser = argparse.ArgumentParser(description='Run external ball algorithm for on standard input')
    parser.add_argument('-d', '--delimiter', nargs='?', default=',', dest='delim')
    args = parser.parse_args()
    
    (center, radius) = streamMEB((map(float, line.split(args.delim)) for line in sys.stdin))
    
    print '%.40s... %f' % (center, radius)
    
    return None
    
if __name__ == '__main__':
	#meb_kl((e,e,e,e,e), 1, (e**2, e**1.5, e**2.5, e**2, e**3))
	#set1_meb_kl()
    main()

