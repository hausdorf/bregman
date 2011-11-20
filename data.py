import random

# A series of helper and utility functions relating to our dataset. Some of
# them generate data, some of the process data, and so on.


# Generates n random Dirichlet samples, with base vector parameter params
def dirichlet(n, params):
	for i in range(n):
		d = len(params)

		# Create d random numbers, sample from Gamma for each, then
		# normalize to 1; this is a reasonable approximation of x ~ Dir
		smp = [random.gammavariate(a,1) for a in params]
		yield [v/sum(smp) for v in smp]


if __name__ == '__main__':
	# Test the Dirichlet generator
	for vec in dirichlet(3, [2,3,4]):
		print vec, sum(d)
