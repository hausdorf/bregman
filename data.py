import random

# A series of helper and utility functions relating to our dataset. Some of
# them generate data, some of the process data, and so on.


# Generates n random Dirichlet samples, each with d dimensions
def dirichlet(n, d):
	for i in range(n):
		# Create d random numbers, sample from Gamma for each, then
		# normalize to 1; this is a reasonable approximation of x ~ Dir
		smp = [random.gammavariate(random.random(),1) for a in range(d)]
		yield [v/sum(smp) for v in smp]


if __name__ == '__main__':
	# Test the Dirichlet generator
	for d in dirichlet(3, 3):
		print d
