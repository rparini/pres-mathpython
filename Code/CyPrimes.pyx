from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from math import sqrt

### just typing the integers in the loops 
def sieve_of_eratosthenes_inti(int n):
	cdef int i, j

	A = [True]*(n+1)
	for i in range(2, int(sqrt(n))+1): 
		if A[i] == True:
			for j in range(i**2, n+1, i):
				A[j] = False

	return [i for i in range(2,n+1) if A[i] == True]


### For more on memory allocation in Cython see:
# http://cython.readthedocs.io/en/latest/src/tutorial/memory_allocation.html
# https://github.com/cython/cython/wiki/DynamicMemoryAllocation
def sieve_of_eratosthenes_malloc(int n):
	# manually allocate (n+1)*sizeof(bint) bytes of memory
	cdef bint* A = <bint *>PyMem_Malloc((n+1) * sizeof(bint))
	cdef int i, j

	if not A:
		raise MemoryError()

	try:
		for i in range(2,n+1):
			A[i] = True

		for i in range(2, int(sqrt(n))+1):
			if A[i] == True:
				for j in range(i**2, n+1, i):
					A[j] = False

		return [i for i in range(2,n+1) if A[i] == True]

	finally:
		# free allocated memory after use
		PyMem_Free(A)

