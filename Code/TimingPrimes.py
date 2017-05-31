# How long does it take to get all the primes up to 1 million?
import timeit
# repeat a few times to get the most repeatable result
repeat = 1000
print('Repeat', repeat)
PyPrimes = min(timeit.repeat(stmt='sieve_of_eratosthenes(1000000)', setup='from Primes import sieve_of_eratosthenes', number=1, repeat=repeat))
print('Original time  ', PyPrimes, '\n')

# pyximport will conveniently compile CPrimes if necessary
import pyximport
pyximport.install()

# ~ 1.8x faster than original python
CyPrimes_inti = min(timeit.repeat(stmt='sieve_of_eratosthenes_inti(1000000)', setup='from CyPrimes import sieve_of_eratosthenes_inti', number=1, repeat=repeat))
print('Typing i,j time', CyPrimes_inti)
print(PyPrimes/CyPrimes_inti, 'x faster\n')

# ~ 3.5x faster than original python
CyPrimes_malloc = min(timeit.repeat(stmt='sieve_of_eratosthenes_malloc(1000000)', setup='from CyPrimes import sieve_of_eratosthenes_malloc', number=1, repeat=repeat))
print('Malloc time    ', CyPrimes_malloc)
print(PyPrimes/CyPrimes_malloc, 'x faster\n')

# run "python CppPrimesSetup.py build_ext --inplace -f" to compile the c++ wrapping
from subprocess import call
call(["python3", "CppPrimesSetup.py", "build_ext", "--inplace"])

# ~ 28x faster than original python
CyPrimes_cpp = min(timeit.repeat(stmt='sieve_of_eratosthenes_cpp(1000000)', setup='from CppPrimes_caller import sieve_of_eratosthenes_cpp', number=1, repeat=repeat))
print('C++ -> Py time ', CyPrimes_cpp)
print(PyPrimes/CyPrimes_cpp, 'x faster\n')

# ~ 39x faster than original python
NpPrimes_cpp = min(timeit.repeat(stmt='sieve_of_eratosthenes_np(1000000)', setup='from NumpyPrimes import sieve_of_eratosthenes_np', number=1, repeat=repeat))
print('NumPy time     ', NpPrimes_cpp)
print(PyPrimes/NpPrimes_cpp, 'x faster')

# check that we get the same answer as the original Python function!
import numpy as np
import Primes
from CyPrimes import sieve_of_eratosthenes_inti
from CyPrimes import sieve_of_eratosthenes_malloc
from CppPrimes_caller import sieve_of_eratosthenes_cpp
from NumpyPrimes import sieve_of_eratosthenes_np

N = 1e6
primes = Primes.sieve_of_eratosthenes(N)
print(np.all(np.array(primes) - np.array(sieve_of_eratosthenes_inti(N)) == 0))  # = True
print(np.all(np.array(primes) - np.array(sieve_of_eratosthenes_malloc(N)) == 0))  # = True
print(np.all(np.array(primes) - np.array(sieve_of_eratosthenes_cpp(N)) == 0))  # = True
print(np.all(np.array(primes) - np.array(sieve_of_eratosthenes_np(N)) == 0))  # = True
