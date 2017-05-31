"""
Sieve of Eratosthenes, derived from the pseudocode on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Input: an integer n > 1

Let A be an array of Boolean values, indexed by integers 2 to n,
initially all set to true.
 
for i = 2, 3, 4, ..., not exceeding \sqrt{n}:
  if A[i] is true:
    for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n:
      A[j] := false
 
Output: all i such that A[i] is true.
"""
from math import sqrt

def sieve_of_eratosthenes(n):
	"""
	Returns a list of all primes not exceeding n using the Sieve of Eratosthenes.
	"""
	n = int(n)
	# A is a list of booleans indexed from 0 to n
	A = [True]*(n+1)						

	# iterate over 2 <= i <= sqrt(n)
	# Note that all non-primes <= n will have a factor <= sqrt(n)
	for i in range(2, int(sqrt(n))+1): 		
		if A[i] == True:
			# Eliminates multiples of each prime i starting from i^2 
			# since smaller multiples will have factors < i
			for j in range(i**2, n+1, i):
				A[j] = False

	# return indicies from 2 to n that are primes
	return [i for i in range(2,n+1) if A[i] == True]	



if __name__ == '__main__':
	# primes up to and including 47
	print(sieve_of_eratosthenes(47))

	# The line 'n = int(n)' in the function allows us to also use floats
	print(sieve_of_eratosthenes(47.6))

