from math import log, exp, e
from scipy.optimize import brentq
import cvxmod
from cvxmod.atoms import norm1
from cvxmod.sets import probsimp


def f(l, p1, p2, r):
	return d(x(p1, p2, l), p2) - r

def d(p1, p2):
	dst = sum([x_i * log(x_i / y_i) - (x_i - y_i)
		for x_i, y_i in zip(p1, p2)])
	return dst

def x(p, c, lamb):
	d_p = [log(p_i) + 1 for p_i in p]
	d_c = [log(c_i) + 1 for c_i in c]
	x_l = [exp((1-lamb) * p_i + lamb * c_i - 1)
			for p_i, c_i in zip(d_p,d_c)]
	return x_l

def search_helper(l_far, l_c, p, c):
	res1 = d(x(p, c, l_far), x(p, c, l_c))
	res2 = d(p, x(p, c, l_c))
	if res1 < res2:
		return -1
	elif res1 > res2:
		return 1
	else:
		return 0

def bsearch(func, lower, upper):
	l_c = (lower + upper) / 2
	c = func(l_c)

	if c == 0:
		return l_c
	elif c < 0:
		return bsearch(func, lower, l_c - 1)
	else:
		return bsearch(func, l_c + 1, upper)

# meb_kl : point c -> radius r -> point p -> point p_far
# each point c, p, and p_far are d-dimensional
def meb_kl(c, r, p):
	f_of_c = f(1, p, c, r)
	x_lamb = x(p, c, 1)
	l_far = brentq(f, 1, 300, args=(p, c, r))
	print d(x(p, c, l_far), c)
	l_c = bsearch(lambda x: search_helper(l_far, x, p, c), 0, l_far)
	print d(x(p, c, l_far), x(p, c, l_c)), d(p, x(p, c, l_c))


if __name__ == '__main__':
	meb_kl((e,e,e,e,e), 1, (e**2, e**1.5, e**2.5, e**2, e**3))
