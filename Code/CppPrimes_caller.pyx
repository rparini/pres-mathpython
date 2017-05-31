from libcpp.vector cimport vector

### import the c++ function 'sieve_of_eratosthenes' from the file "CppPrimes.cpp"
cdef extern from "CppPrimes.cpp":
	vector[int] sieve_of_eratosthenes(int n)

### wrap the c++ function
def sieve_of_eratosthenes_cpp(int n):
	return sieve_of_eratosthenes(n)
