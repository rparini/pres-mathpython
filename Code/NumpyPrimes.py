from math import sqrt
import numpy as np
def sieve_of_eratosthenes_np(n):
	"""
	Returns an np.array of all primes not exceeding n using the Sieve of Eratosthenes.
	"""
	n = int(n)
	A = np.ones(n+1, dtype=bool)
	A[:2] = False # 0 and 1 are not primes
	
	# Note that all composite numbers <= n will have a factor <= sqrt(n)
	for i in range(2, int(sqrt(n))+1):
		if A[i] == True:
			# Eliminates multiples of each prime i starting from i^2 
			# since smaller multiples will have factors < i
			A[i**2:n+1:i] = False

	return np.nonzero(A)[0]	# return indicies from 2 to n that are primes



if __name__ == '__main__':
	# primes up to and including 47
	print(sieve_of_eratosthenes_np(47))

	# The line 'n = int(n)' in the function allows us to also use floats
	print(sieve_of_eratosthenes_np(47.6))

